from tornado import escape

from models.show import Show, Cast
from rbac.role import Role
from schemas.schemas import CastSchema
from utils.web.base_controller import BaseAPIController
from utils.web.web_decorators import requires_show, no_live_session
from utils.web.route import ApiRoute, ApiVersion


@ApiRoute('show/cast', ApiVersion.V1)
class CastController(BaseAPIController):

    @requires_show
    def get(self):
        current_show = self.get_current_show()
        show_id = current_show['id']
        cast_schema = CastSchema()

        with self.make_session() as session:
            show = session.query(Show).get(show_id)
            if show:
                cast = [cast_schema.dump(c) for c in show.cast_list]
                self.set_status(200)
                self.finish({'cast': cast})
            else:
                self.set_status(404)
                self.finish({'message': '404 show not found'})

    @requires_show
    @no_live_session
    async def post(self):
        current_show = self.get_current_show()
        show_id = current_show['id']

        with self.make_session() as session:
            show = session.query(Show).get(show_id)
            if show:
                self.requires_role(show, Role.WRITE)
                data = escape.json_decode(self.request.body)

                first_name = data.get('firstName', None)
                if not first_name:
                    self.set_status(400)
                    await self.finish({'message': 'First name missing'})
                    return

                last_name = data.get('lastName', None)
                if not last_name:
                    self.set_status(400)
                    await self.finish({'message': 'Last name missing'})
                    return

                session.add(Cast(show_id=show.id, first_name=first_name, last_name=last_name))
                session.commit()

                self.set_status(200)
                await self.finish({'message': 'Successfully added cast member'})

                await self.application.ws_send_to_all('GET_CAST_LIST', 'GET_CAST_LIST', {})
            else:
                self.set_status(404)
                await self.finish({'message': '404 show not found'})

    @requires_show
    @no_live_session
    async def patch(self):
        current_show = self.get_current_show()
        show_id = current_show['id']

        with self.make_session() as session:
            show = session.query(Show).get(show_id)
            if show:
                self.requires_role(show, Role.WRITE)
                data = escape.json_decode(self.request.body)

                cast_id = data.get('id', None)
                if not cast_id:
                    self.set_status(400)
                    await self.finish({'message': 'ID missing'})
                    return

                entry: Cast = session.get(Cast, cast_id)
                if entry:
                    first_name = data.get('firstName', None)
                    if not first_name:
                        self.set_status(400)
                        await self.finish({'message': 'First name missing'})
                        return
                    entry.first_name = first_name

                    last_name = data.get('lastName', None)
                    if not last_name:
                        self.set_status(400)
                        await self.finish({'message': 'Last name missing'})
                        return
                    entry.last_name = last_name

                    session.commit()

                    self.set_status(200)
                    await self.finish({'message': 'Successfully updated cast member'})

                    await self.application.ws_send_to_all('GET_CAST_LIST', 'GET_CAST_LIST', {})
                else:
                    self.set_status(404)
                    await self.finish({'message': '404 cast member not found'})
                    return
            else:
                self.set_status(404)
                await self.finish({'message': '404 show not found'})

    @requires_show
    @no_live_session
    async def delete(self):
        current_show = self.get_current_show()
        show_id = current_show['id']

        with self.make_session() as session:
            show = session.query(Show).get(show_id)
            if show:
                self.requires_role(show, Role.WRITE)
                data = escape.json_decode(self.request.body)

                cast_id = data.get('id', None)
                if not cast_id:
                    self.set_status(400)
                    await self.finish({'message': 'ID missing'})
                    return

                entry = session.get(Cast, cast_id)
                if entry:
                    session.delete(entry)
                    session.commit()

                    self.set_status(200)
                    await self.finish({'message': 'Successfully deleted cast member'})

                    await self.application.ws_send_to_all('GET_CAST_LIST', 'GET_CAST_LIST', {})
                else:
                    self.set_status(404)
                    await self.finish({'message': '404 cast member not found'})
            else:
                self.set_status(404)
                await self.finish({'message': '404 show not found'})
