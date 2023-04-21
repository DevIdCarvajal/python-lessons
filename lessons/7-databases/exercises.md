# Ejercicios

## tobtahC

Se pide desarrollar un chatbot con sockets cuyo comportamiento sea el siguiente:

### Nivel 1 (easy mode)

Por cada cliente que le envíe un mensaje, el servidor le responderá lo mismo pero con el mensaje invertido.

Nota: Tanto clientes como servidor se ejecutarán localmente.

### Nivel 2 (normal mode)

Además de lo anterior, almacenará en una base de datos toda la conversación, anotando la IP del cliente, el mensaje y el timestamp.

### Nivel 3 (hard mode)

Además de lo anterior, el servidor debe ser capaz de atender a tres clientes simultáneamente, generando un thread para cada uno de ellos.

### Nivel 14 (singularity mode)

Colaborar con otros compañeros para montar una red local en la que los clientes de uno hablen con los servidores de otros.