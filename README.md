# Traducciones compartidas de Traductor ES

Traducciones al español de mods de Minecraft hechas con [Traductor ES](https://github.com/luchomart/traductor-es).
El mod las descarga antes de usar la IA: si alguien ya tradujo un mod, no hace falta gastar cupo ni esperar.
La descarga se puede apagar desde el panel del mod.

## Formato
Una carpeta por variante del español y un archivo por mod (o por libro: Patchouli, GuideME, Manual de IE…).

```
index.json                          lista de archivos con un hash, para bajar solo lo que cambió
es_ar/ae2.json
es_ar/@patchouli__ae2__guide.json
```

Cada archivo tiene dos secciones, con el **texto en inglés como clave** (así sirve aunque el mod se actualice):

```json
{
 "revisadas": { "ME Drive": "Unidad ME" },
 "ia": { "Portable Fuel Interface": "Interfaz portátil de combustible" }
}
```

- `revisadas`: las revisó una persona. Tienen prioridad.
- `ia`: las hizo la IA y pasaron los controles del mod, pero nadie las leyó.

Las misiones de FTB Quests y las fichas de REI son de cada modpack y no van acá (por ahora).

## Aportar
1. Traducí con el mod y corregí lo que haga falta con el editor del juego (las correcciones entran como revisadas).
2. Hacé un fork de este repo y cloná tu fork.
3. Con [`tools/compartir.py`](https://github.com/luchomart/traductor-es/blob/main/tools/compartir.py) del repo del mod:
   ```
   python3 compartir.py "<carpeta de tu instancia>" --repo <carpeta de tu fork>
   ```
   La variante (es_ar, es_es…) sale sola de la que usaste en el juego. Lo que ya está en el repo no se pisa.
4. Revisá: `python3 herramientas/validar.py`, y abrí un pull request.

Para mejorar una traducción a mano: editala y pasala de `ia` a `revisadas`. Después, `python3 herramientas/validar.py --indice`.

## Licencia
[CC BY-NC-SA 4.0](LICENSE). Los textos originales pertenecen a los autores de cada mod.
