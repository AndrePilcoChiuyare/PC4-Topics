from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class TorreAgent(Agent):
    pista_ocupada = False

    class TowerBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=5)
            if msg:
                print(f"{self.agent.name}: reporte de {msg.sender}")
                reply = Message(to=str(msg.sender))
                content = msg.body

                if content == "volando":
                    reply.set_metadata("performative", "inform")
                    reply.body = "recibido"
                elif content == "aterrizar":
                    if TorreAgent.pista_ocupada:
                        reply.set_metadata("performative", "reject-proposal")
                        reply.body = "rechazo"
                    else:
                        print(f"{self.agent.name}: permiso para {msg.sender}")
                        reply.set_metadata("performative", "accept-proposal")
                        reply.body = "aceptar"
                        TorreAgent.pista_ocupada = True
                else:
                    reply.set_metadata("performative", "not-understood")
                    reply.body = "desconocido"

                await self.send(reply)

    async def setup(self):
        self.add_behaviour(self.TowerBehaviour())
