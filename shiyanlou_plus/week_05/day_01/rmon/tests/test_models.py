from rmon.models import Server
from rmon.common.rest import RestException


class TestServer:

    def test_save(self, db):
        assert Server.query.count() == 0
        server = Server(name="test", host="127.0.0.1")
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self, db, server):
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0

    def test_ping_success(self, db, server):
        assert server.ping() is True

    def test_ping_failed(self, db):
        server = Server(name="test", host="127.0.0.1")
        try:
            server.ping()
        except RestException as e:
            assert e.code == 400
            assert e.message == "redis server %s can not connected" %
                server.host

    def test_get_metrics_success(self, server):
        metrics = server.get_metrics()

        assert "total_commands_processed" in metrics
        assert "used_cpu_sys" in metrics
        assert "used_memory" in metrics

    def test_get_metrics_failed(self, server):
        server = Server(name="test", host="127.0.0.1", port=6379)

        try:
            info = server.get_metrics()
        except RestException as e:
            assert e.code == 400
            assert e.message == "redis server %s cannot connected" %
                server.host

    def test_execute_success(self, server):
        pass

    def test_execute_failed(self, server):
        pass
