from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour, PeriodicBehaviour
from spade.message import Message
import asyncio

class TorreAgent:
    pista_ocupada = False

class AvionAgent(Agent):
    class FlightBehaviour(PeriodicBehaviour):
        async def run(self):
            print(f"({self.agent.name})")

    class ReportBehaviour(PeriodicBehaviour):
        async def run(self):
            msg = Message(to="torre@localhost")
            msg.body = "volando"
            msg.set_metadata("performative", "inform")
            await self.send(msg)

    class RequestLandBehaviour(PeriodicBehaviour):
        async def run(self):
            msg = Message(to="torre@localhost")
            msg.body = "aterrizar"
            msg.set_metadata("performative", "propose")
            await self.send(msg)

    class ListenBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=5)
            if msg:
                if msg.body == "recibido":
                    print(f"-> {self.agent.name} confirmación de la Torre")
                elif msg.body == "aceptar":
                    TorreAgent.pista_ocupada = True
                    self.agent.add_behaviour(self.agent.LandingBehaviour())
                elif msg.body == "rechazo":
                    print(f"-> {self.agent.name} rechazo de la Torre")

    class LandingBehaviour(OneShotBehaviour):
        async def run(self):
            print(f"=> {self.agent.name} (inicio aterrizaje)")
            await asyncio.sleep(2)
            print(f"=> {self.agent.name} (fin aterrizaje)")
            TorreAgent.pista_ocupada = False
            await self.agent.stop()

    async def setup(self):
        self.add_behaviour(self.FlightBehaviour(period=1))
        self.add_behaviour(self.ReportBehaviour(period=5))
        self.add_behaviour(self.RequestLandBehaviour(period=10))
        self.add_behaviour(self.ListenBehaviour())
