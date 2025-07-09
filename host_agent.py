from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from avion_agent import AvionAgent
from torre_agent import TorreAgent

class HostAgent(Agent):
    numero_aviones = 10

    class LaunchBehaviour(OneShotBehaviour):
        async def run(self):
            torre_jid = "torre@localhost"
            torre = TorreAgent(torre_jid, "p4ssword")
            await torre.start()

            for i in range(self.agent.numero_aviones):
                name = f"avion_{i+1}@localhost"
                avion = AvionAgent(name, "p4ssword")
                await avion.start()

    async def setup(self):
        self.add_behaviour(self.LaunchBehaviour())
