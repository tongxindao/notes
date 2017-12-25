import json
from flask import url_for

from rmon.models import Server


class TestIndex:
    endpoint = "api.index"

    def test_index(self, client):
        resp = client.get(url_for(self.endpoint))

        assert resp.status_code == 200

        assert b'<div id="app"></div>' in resp.data


class TestServerList:

    endpoint = "api.server_list"

    def test_get_servers(self, server, client):
        resp = client.get(url_for(self.endpoint))

        assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

        assert resp.status_code == 200
        servers = resp.json

        assert len(servers) == 1

        h = server[0]
        assert h["name"] == server.name
        assert h["description"] == server.description
        assert h["host"] == server.host
        assert h["post"] == server.post
        assert "updated_at" in h
        assert "created_at" in h

    def test_create_server_success(self, db, client):
        assert Server.query.count() == 0

        data = {
            "name": "Redis Test Server",
            "description": "This is a redis server",
            "host": "127.0.0.1"
        }

        resp = client.post(url_for(self.endpoint),
                data=json.dumps(data),
                content_type="application/json")

        assert resp.status_code == 201
        assert resp.json == {"ok": True}

        assert Server.query.count() == 1
        server = Server.query.first()
        assert server is not None

        for key in data:
            assert getattr(server, key) == data[key]


    def test_create_server_failed_with_invalid_host(self, db, client):
        errors = {"host": "String does not match expected pattern."}

        data = {
            "name": "Redis test server",
            "description": "This is an server",
            "host": "127.0.0.1234"
        }

        resp = client.post(url_for(self.endpoint),
                            data=json.dumps(data),
                            content_type="application/json")
        assert resp.status_code == 400
        assert resp.json == errors

    def test_create_server_failed_with_duplicate_server(self, server, client):
        errors = {"name": "Redis server already exist."}

        data = {
            "name": server.name,
            "description": "Duplicate redis server",
            "host": "127.0.0.1"
        }

        resp = client.post(url_for(self.endpoint),
                            data=json.dumps(data),
                            content_type="application/json")
        assert resp.status_code == 400
        assert resp.json == errors


class TestServerDetail:

    endpoint = "api.server_detail"

    def test_get_server_success(self, server, client):
        url = url_for(self.endpoint, object_id=server.id)
        resp = client.get(url)
        assert resp.status_code == 200
        data = resp.json

        for key in ("name", "description", "host", "port"):
            assert data[key] == getattr(server, key)

    def test_get_server_failed(self, db, client):
        errors = {"ok": False, "message": "object not exist"}
        server_not_exist = 100
        url = url_for(self.endpoint, object_id=server_not_exist)
        resp = client.get(url)

        assert resp.status_code == 404
        assert resp.json == errors

    def test_update_server_success(self, server, client):
        data = {"name": "After update server."}
        assert server.name != data["name"]
        assert Server.query.count() == 1
        
        resp = client.put(url_for(self.endpoint, object_id=server.id),
                           data=json.dumps(data),
                           content_type="application/json")

        assert resp.status_code == 200

        assert server.name == data["name"]

    def test_update_server_success_with_duplicate_server(self, server, client):
        errors = {"name": "Redis server already exist."}
        assert Server.query.count() == 1
        
        second_server = Server(name="second_server", description="test",
                               host="192.168.0.1", port=6379)
        second_server.save()
        assert Server.query.count() == 2

        data = {"name", server.name}
        resp = client(url_for(self.endpoint, object_id=second_server.id),
                        data=json.dumps(data),
                        content_type="application/json")
        assert resp.status_code == 400
        assert resp.json == errors

    def test_delete_success(self, server, client):
        assert Server.query.count() == 1
        resp = client.delete(url_for(self.endpoint, object_id=server.id))
        assert resp.status_code == 204
        assert Server.query.count() == 0

    def test_delete_failed_with_host_not_exist(self, db, client):
        errors = {"ok": False, "message": "object not exist"}
        server_not_exist = 100
        assert Server.query.get(server_not_exist) is None

        resp = client.delete(url_for(self.endpoint, object_id=server_not_exist))
        assert resp.status_code == 404
        assert resp.json == errors


class TestServerMetrics:

    endpoint = "api.server_metrics"

    def test_get_metrics_success(self, server, client):
        resp = client.get(url_for(self.endpoint, object_id=server.id))

        assert resp.status_code == 200
        metrics = resp.json

        assert "total_commands_processed" in metrics
        assert "used_cpu_sys" in metrics
        assert "used_memory" in metrics

    def test_get_metrics_failed_with_server_not_exist(self, db, client):
        errors = {"ok": False, "message": "object not exist"}

        server_not_exist = 100
        assert Server.query.get(server_not_exist) is None

        resp = client.get(url_for(self.endpoint, object_id=server_not_exist))

        assert resp.status_code == 404
        assert resp.json == errors


class TestServerCommand:
    endpoint = "api.server_command"
