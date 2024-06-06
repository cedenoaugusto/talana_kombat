Prueba de admision para Talana.

Talana Kombat JRPG

el pdf tiene un error. Donde dice: "Tonyn le da un puñetazo al pobre Arnaldor" lo que realmente sucede es un movimiento del personaje de acuerdo a JSON.
Por lo tanto al ganar Arnaldor le quedan 2 de energía, no 1 como se plantea en el ejemplo.

--
Respuesta Preguntas generales:
1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. 
Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.
De ser posible, que quede solo un commit con los cambios.
Se podria solucionar haciendo el comando para restablecer el repo.
un git reset --{soft/hard/mixed}
y luego subir los cambios.
git add .
git commit -m "..."
git push

Si no aun haces push, entonces:
git add mi_archivo_faltante.py
git commit -m "..."
git push

2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
    - Cambios requeridoes en rama DEV, 
    - Luego merge a la rama QA, y 
    - Finalmente merge a la rama PROD.

3.¿Cuál ha sido la situación más compleja que has tenido con esto?
Realizar merge cuando se topan cambios sobre el mismo archivo.

4. ¿Qué experiencia has tenido con los microservicios?
Creacion de cloud functions de GCP, para separar procesos.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?
GCP, porque es el que aprendí a usar.