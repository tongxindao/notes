from flask import request, g

from rmon.common.rest import RestView
from rmon.common.decorators import ObjectMustBeExist
from rmon.models import Server, ServerSchema


class ServerList(RestView):

    def get(self):
        # get redis list
        servers = Server.query.all()
        return ServerSchema().dump(servers, many=True).data

    def post(self):
        # create redis server
        data = request.get_json()
        server, errors = ServerSchema().load(data)
        if errors:
            return errors, 400
        server.ping()
        server.save()
        return {"ok": True}, 201


class ServerDetail(RestView):

    method_decorators = (ObjectMustBeExist(Server), )

    def get(self, object_id):
        """
        get server detail
        """
        data, _ = ServerSchema().dump(g.instance)
        return data

    def put(self, object_id):
        """
        update server
        """
        schema = ServerSchema(context={"instance": g.instance})
        data = request.get_json()
        server, errors = schema.load(data, partial=True)
        if errors:
            return errors, 400
        server.save()
        return {"ok": True}

    def delete(self, object_id):
        """
        delete server
        """
        g.instance.delete()
        return {"ok": True}, 204


class ServerMetrics(RestView):

    method_decorators = (ObjectMustBeExist(Server), )
    
    def get(self, object_id):
        return g.instance.get_metrics()


class ServerCommand(RestView):

    method_decorators = (ObjectMustBeExist(Server), )

    def post(self, object_id):
        pass
