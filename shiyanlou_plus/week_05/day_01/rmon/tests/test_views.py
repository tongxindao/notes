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
        pass

    def test_create_server_failed_with_duplicate_server(self, server, client):
        pass


class TestServerDetail:

    endpoint = "api.server_detail"

    def test_get_server_success(self, server, client):
        pass

    def test_get_server_failed(self, db, client):
        pass

    def test_update_server_success(self, server, client):
        pass

    def test_update_server_success_with_duplicate_server(self, server, client):
        pass

    def test_delete_success(self, server, client):
        pass

    def test_delete_failed_with_host_not_exist(self, db, client):
        pass


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
