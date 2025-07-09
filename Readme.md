# Práctica Calificada 4
- André Dario Pilco Chiuyare - U202110764
- Renzo Andree Espíritu Cueva - U202113340
- Luis Felipe Poma Astete - U202110902
- John Davids Sovero Cubillas - U202115065

## (3 puntos) Detallar el proceso de configuración de SPADE y componentes.

Después de instalar Rust (`https://rustup.rs/`), para el correcto funcionamiento SPADE, se utilizó la imagen Docker de OpenFire del usuario sameersbn a través de `docker pull sameersbn/openfire:latest`. Luego, se instaló la librería `spade` mediante la sentencia `pip install spade`. Por último, se ejecutó el servidor a través de `docker run --name openfire -d --restart=always  --publish 9090:9090 --publish 5222:5222 --publish 7777:7777 --volume /srv/docker/openfire:/var/lib/openfire sameersbn/openfire:latest`.

Una vez iniciado el servidor XMPP con Docker, se ingresó a él a través de `http://localhost:9090` y se inicializó el dominio como `localhost`, se establecieron las credenciales de administrador y se seleccionó una base de datos embebida. Por último, se creó manualmente un usuario `torre` y diez para los aviones (`avion_n`).

En cuanto a los componentes del sistema multiagente que utilizan el servidor XMPP como para la comunicación, se tienen tres principales:
- **Avión:** Representa un avión que realiza tareas periódicas y escucha instrucciones como mostrar su nombre cada cierto tiempo, informar que está volando, solicitar permiso para aterrizar, esperar respuestas de la torre y aterrizar.
- **Torre:** Representa la torre de control y puede recibir mensajes de los aviones, por lo que responde `recibido` ante la información de vuelo y puede aceptar o rechazar solicitudes de aterrizaje, dependiendo si la pista está ocupada.
- **Host:** Agente principal que inicia todos los demás, ya que crea y ejecuta la torre junto a los diez aviones.

## (3 puntos) Incluya un comentario de la opinión del grupo respecto a las ventajas y desventajas de SPACE vs JADE.
Tanto SPADE como JADE son herramientas potentes para el desarrollo de sistemas multiagente, pero tienen características que diferencian su utilidad dependiendo del contexto del proyecto:
**Ventajas de SPADE frente a JADE**
- Simplicidad y rapidez de desarrollo: SPADE, al estar basado en Python, facilita la integración con otras librerías y la definición de agentes de manera concisa, agilizando el proceso de desarrollo.
- Integración con herramientas modernas: SPADE es más fácil de combinar con bibliotecas de machine learning, APIs REST y bases de datos.
- Facilidad de despliegue: Con el uso de Docker y servidores XMPP como OpenFire, es posible desplegar entornos completos rápidamente.

**Desventajas respecto a JADE**
- Comunidad: JADE, al tener más años de desarrollo, presenta una comunidad más grande y documentación más extensa.
- Soporte a estándares FIPA: JADE cumple de forma más completa con los estándares FIPA, mientras que SPADE tiene implementaciones más ligeras.
- Herramientas de monitoreo: JADE incluye herramientas gráficas integradas para monitorear los agentes, lo cual es útil en entornos complejos. Para lograr un comportamiento similar en SPADE, es necesario implementarlas manualmente o recurrir a herramientas externas.
