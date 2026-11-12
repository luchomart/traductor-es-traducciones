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
Traducí con el mod y corregí lo que haga falta con el editor del juego (las correcciones entran como revisadas).
Después, en el juego: **Herramientas → Compartir…**

- **Enviar a la comunidad** (lo más fácil): la primera vez te pide conectar tu cuenta de GitHub con un código;
  después, un clic. El mod sube tus traducciones nuevas y abre el pull request por vos.
- **Exportar carpeta** (sin conectar la cuenta): el mod arma una carpeta `es_ar/` (o la de tu variante) y abre la
  página de subida de este repo. Arrastrá esa carpeta, pegá el título que el mod ya copió (Ctrl+V) y tocá *Propose changes*.

En los dos casos la variante sale sola, y cada archivo ya trae lo que estaba en el repo más lo tuyo: no se pisa nada.
Un control automático revisa cada pull request antes de aceptarlo. `index.json` no se toca: se rehace solo.

Para muchos modpacks a la vez está [`tools/compartir.py`](https://github.com/luchomart/traductor-es/blob/main/tools/compartir.py)
del repo del mod. Para mejorar una traducción a mano: editala y pasala de `ia` a `revisadas`.

## Licencia
[CC BY-NC-SA 4.0](LICENSE). Los textos originales pertenecen a los autores de cada mod.
