# Base de datos masiva definitiva de OLYMPUS Cybermuseum

SPORTS_DATABASE = {
    "hockey-hielo": {
        "id": "hockey-hielo",
        "name": "Hockey sobre Hielo",
        "category": "Invierno",
        "tagline": "Velocidad extrema sobre cuchillas a 50 km/h, discos a 160 km/h y batallas colosales en la NHL.",
        "primary_color": "#00f2fe",
        "secondary_color": "#ff007f",
        "icon_symbol": "🏒",
        "history_long": """Nacido a mediados del siglo XIX en los estanques congelados de Canadá, el hockey sobre hielo combina la máxima intensidad de contacto físico con una destreza técnica quirúrgica. La creación de la National Hockey League (NHL) consolidó a este deporte como la disciplina invernal más vibrante, rápida y tácticamente compleja del planeta.

Los partidos se disputan sobre una pista de hielo refrigerada rodeada de acrílicos protectores, donde dos equipos de seis jugadores patinan a velocidades cercanas a los 50 km/h. La introducción del tiempo neto cronometrado, los cambios de jugadores 'al vuelo' sin detener el juego y la evolución de tácticas defensivas y ofensivas han transformado el hockey en un espectáculo global seguido por millones de fanáticos en Norteamérica, Europa y Asia.""",
        "timeline": [
            {"era": "Orígenes e Invención (1875 - 1917)", "icon": "📜", "desc": "Nacimiento formal en los lagos congelados de Canadá y establecimiento de la Copa Stanley."},
            {"era": "Consolidación y Era Dorada (1917 - 2000)", "icon": "🏒", "desc": "Expansión de la NHL con los 'Original Six', cascos obligatorios y dominio histórico mundial."},
            {"era": "Era Global y Moderna (2000 - 2026)", "icon": "⚡", "desc": "Talento internacional masivo y analítica avanzada mediante chips de rastreo en el puck."}
        ],
        "rules_and_tactics": [
            {"title": "Pista y Acrílicos", "desc": "Superficie de 60x30m rodeada de muros acrílicos con cristal templado."},
            {"title": "Cambios al Vuelo", "desc": "3 periodos de 20 minutos de tiempo real con sustituciones dinámicas sin detener el reloj."}
        ],
        "leagues_and_nations": ["NHL (EE.UU. y Canadá)", "KHL (Europa / Asia)", "Potencias: Canadá, Rusia, Suecia, Finlandia"],
        "teams_and_franchises": [
            "Montreal Canadiens &mdash; 24 Stanley Cups",
            "Toronto Maple Leafs &mdash; 13 Stanley Cups",
            "Detroit Red Wings &mdash; 11 Stanley Cups"
        ],
        "legends": [
            {"name": "Wayne Gretzky", "nickname": "The Great One", "country": "Canadá", "stat": "2,857 Puntos", "bio": "El máximo anotador y estratega en la historia del deporte profesional norteamericano."},
            {"name": "Marie-Philip Poulin", "nickname": "Captain Clutch", "country": "Canadá", "stat": "4 Oros Olímpicos", "bio": "La atleta más determinante en la historia del hockey femenino mundial."}
        ]
    },
    "patinaje-artistico": {
        "id": "patinaje-artistico",
        "name": "Patinaje Artístico",
        "category": "Invierno",
        "tagline": "Gravedad desafiada sobre cuchillas: saltos cuádruples, giros vertiginosos y arte escénico sobre hielo.",
        "primary_color": "#bd00ff",
        "secondary_color": "#00f2fe",
        "icon_symbol": "⛸️",
        "history_long": """El patinaje artístico sobre hielo es la disciplina invernal más elegante y técnica de los Juegos Olímpicos, integrada formalmente desde Londres 1908. Combina la precisión física extrema de saltos con múltiples rotaciones en el aire con la máxima expresión coreográfica, musical y artística del deporte mundial.""",
        "timeline": [
            {"era": "Inicios (Siglo XIX)", "icon": "📜", "desc": "Evolución de figuras obligatorias sobre hielo en Europa y América."},
            {"era": "Debut Olímpico (1908 - 1980)", "icon": "⛸️", "desc": "Inclusión olímpica y estandarización de saltos acrobáticos en solitario y parejas."},
            {"era": "Revolución Cuádruple (1990 - 2026)", "icon": "✨", "desc": "Sistema de juicio abierto ISU y ejecución de saltos cuádruples extremos."}
        ],
        "rules_and_tactics": [
            {"title": "Elementos Técnicos", "desc": "Saltos de rotación múltiple (Axel, Lutz, Salchow) y piruetas sincronizadas."},
            {"title": "Programas", "desc": "Programa Corto (obligatorio) y Programa Libre (coreografía artística total)."}
        ],
        "leagues_and_nations": ["ISU (International Skating Union)", "Grand Prix de Patinaje", "Potencias: Japón, Rusia, EE.UU., Canadá"],
        "teams_and_franchises": ["Escuela Japonesa de Alta Escuela", "Federación Norteamericana"],
        "legends": [
            {"name": "Yuzuru Hanyu", "nickname": "Ice Prince", "country": "Japón", "stat": "Doble Oro Olímpico", "bio": "Primer hombre en aterrizar con éxito el salto cuádruple Loop en competición oficial."},
            {"name": "Kim Yuna", "nickname": "Queen Yuna", "country": "Corea del Sur", "stat": "Campeona Olímpica", "bio": "Famosa por su elegancia impecable y consistencia bajo presión absoluta."}
        ]
    },
    "esqui-alpino": {
        "id": "esqui-alpino",
        "name": "Esquí Alpino",
        "category": "Invierno",
        "tagline": "Descensos suicidas a 140 km/h por pendientes heladas desafiando los límites de la física.",
        "primary_color": "#00ff66",
        "secondary_color": "#00f2fe",
        "icon_symbol": "⛷️",
        "history_long": """El esquí alpino nació en los Alpes europeos a finales del siglo XIX, transformándose rápidamente en la cumbre de la velocidad y el vértigo invernal. Los esquiadores descienden por pendientes montañosas extremadamente empinadas y heladas a velocidades superiores a los 140 km/h, negociando puertas de control con una precisión biomecánica sobrehumana.""",
        "timeline": [
            {"era": "Orígenes Alpinos (1920 - 1950)", "icon": "📜", "desc": "Primeros campeonatos mundiales en Mürren y debut olímpico en Garmisch-Partenkirchen 1936."},
            {"era": "Copa del Mundo FIS (1967 - 2000)", "icon": "⛷️", "desc": "Creación del circuito internacional de la Copa del Mundo y trajes aerodinámicos."},
            {"era": "Élite Moderna (2000 - 2026)", "icon": "⚡", "desc": "Implementación de esquís carving, airbags de seguridad y analítica GPS en tiempo real."}
        ],
        "rules_and_tactics": [
            {"title": "Cronometraje", "desc": "Carreras decididas por milésimas de segundo mediante sensores de alta precisión."},
            {"title": "Puertas", "desc": "El esquiador debe cruzar obligatoriamente por dentro de los pares de banderines."}
        ],
        "leagues_and_nations": ["FIS (Federación Internacional de Esquí)", "Copa del Mundo FIS", "Potencias: Austria, Suiza, Noruega, Italia"],
        "teams_and_franchises": ["Equipo Nacional de Austria (Ski Austria)", "Swiss-Ski"],
        "legends": [
            {"name": "Lindsey Vonn", "nickname": "Speed Queen", "country": "EE.UU.", "stat": "82 Victorias FIS", "bio": "La esquiadora más veloz y dominante de la historia moderna de la Copa del Mundo."},
            {"name": "Marcel Hirscher", "nickname": "El Monstruo", "country": "Austria", "stat": "8 Globos de Cristal", "bio": "Dominador absoluto e indiscutible de la técnica alpina masculina."}
        ]
    },
    "futbol": {
        "id": "futbol",
        "name": "Fútbol (Soccer)",
        "category": "Verano",
        "tagline": "El deporte rey del planeta: pasión de masas, táctica milimétrica y magia en la grama.",
        "primary_color": "#00ff66",
        "secondary_color": "#00f2fe",
        "icon_symbol": "⚽",
        "history_long": """El fútbol moderno se codificó en Inglaterra en 1863 con la fundación de la Football Association, aunque sus raíces históricas de juegos de pelota se remontan a milenios atrás en China, Mesoamérica y Europa medieval. Hoy es indiscutiblemente el deporte más popular, masivo y apasionante del planeta.

La Copa Mundial de la FIFA es el evento deportivo con mayor audiencia global de la historia humana. Desde las calles de Sudamérica hasta los colosos tácticos de Europa, el fútbol enfrenta a 11 jugadores por bando en una sinfonía de estrategia, regates imposibles, lectura táctica del espacio y una devoción cultural incomparable.""",
        "timeline": [
            {"era": "Codificación y Primeras Reglas (1863 - 1930)", "icon": "📜", "desc": "Nacimiento de la FA en Londres, unificación de reglas de Cambridge y la creación de la primera Copa Mundial de la FIFA en Uruguay (1930)."},
            {"era": "La Era de los Gigantes y el Jogo Bonito (1930 - 2000)", "icon": "👑", "desc": "Consolidación de las potencias sudamericanas (Brasil, Argentina) y europeas (Alemania, Italia), con leyendas eternas como Pelé y Maradona."},
            {"era": "Era Global, Científica y Messianic (2000 - 2026)", "icon": "⚡", "desc": "Revolución de la Champions League, el VAR, la ciencia deportiva de alta precisión y la rivalidad histórica entre Lionel Messi y Cristiano Ronaldo."}
        ],
        "rules_and_tactics": [
            {"title": "Duración y Terreno", "desc": "90 minutos divididos en dos tiempos de 45 minutos en canchas de césped natural o sintético de hasta 105x68 metros."},
            {"title": "La Regla del Fuera de Juego (Offside)", "desc": "Un jugador atacante no puede recibir el balón más adelantado que el penúltimo defensa rival al momento del pase."},
            {"title": "Sistemas Tácticos", "desc": "Esquemas dinámicos como el 4-3-3, 4-4-2 o pressing asimétrico moderno liderados por entrenadores de élite."}
        ],
        "leagues_and_nations": [
            "FIFA (Federación Internacional de Fútbol Asociación)",
            "UEFA Champions League & Copa Libertadores",
            "Ligas de Élite: Premier League, LaLiga, Serie A, Bundesliga"
        ],
        "teams_and_franchises": [
            "Real Madrid &mdash; 15 Champions Leagues (Rey indiscutible de Europa)",
            "FC Barcelona &mdash; Filosofía de posesión y academia La Masia",
            "Brasil &mdash; 5 Copas del Mundo FIFA (La pentacampeona mundial)",
            "Argentina &mdash; Campeones del Mundo vigentes (Magia y jerarquía)"
        ],
        "legends": [
            {"name": "Lionel Messi", "nickname": "La Pulga / GOAT", "country": "Argentina", "stat": "8 Balones de Oro & Mundial 2022", "bio": "El jugador más genio y determinante en la historia del fútbol moderno, dotado de una visión y regate inigualables."},
            {"name": "Pelé (Edson Arantes)", "nickname": "O Rei", "country": "Brasil", "stat": "3 Copas del Mundo (Único en la historia)", "bio": "El rey mundial del fútbol, atleta total que transformó el deporte en un arte universal durante el siglo XX."},
            {"name": "Cristiano Ronaldo", "nickname": "CR7", "country": "Portugal", "stat": "900+ Goles Oficiales & 5 Champions", "bio": "El epítome de la ética de trabajo, potencia atlética y voracidad goleadora histórica."},
            {"name": "Diego Armando Maradona", "nickname": "Pibe de Oro", "country": "Argentina", "stat": "Mundial México 1986", "bio": "El genio rebelde del sur, autor del gol del siglo y la magia pura sobre el césped."},
            {"name": "Zinedine Zidane", "nickname": "Zizou", "country": "Francia", "stat": "Campeón del Mundo y de Europa", "bio": "Elegancia absoluta con el balón dominado y una técnica de control celestial."}
        ]
    },
    "baloncesto": {
        "id": "baloncesto",
        "name": "Baloncesto",
        "category": "Verano",
        "tagline": "Gravedad cero en el aire, velocidad de transición y la búsqueda de la precisión táctica en la duela.",
        "primary_color": "#ff6600",
        "secondary_color": "#9a3412",
        "icon_symbol": "🏀",
        "history_long": """El baloncesto fue concebido en diciembre de 1891 por el profesor canadiense James Naismith en la Springfield College de Massachusetts. Buscando un juego de interior para sus estudiantes durante los crudos inviernos, Naismith clavó dos cestas de duraznos en los balcones del gimnasio a 3.05 metros de altura.

Con la fundación de la NBA en 1946 y la participación del 'Dream Team' en Barcelona 1992, el baloncesto explotó como un fenómeno cultural global. La evolución del tiro de tres puntos, las transiciones ultrarrápidas y la preparación física multidisciplinaria han redefinido el juego moderno.""",
        "timeline": [
            {"era": "Invención de Naismith (1891)", "icon": "📜", "desc": "Creación del deporte con cestas de duraznos y 13 reglas originales."},
            {"era": "Nacimiento de la NBA y Dream Team (1946 - 1992)", "icon": "👑", "desc": "Evolución profesional de la liga norteamericana y la internacionalización con los Juegos Olímpicos de Barcelona."},
            {"era": "Era del Espacio y Triples (2000 - 2026)", "icon": "⚡", "desc": "Revolución del spacing táctico, analítica de tiro exterior y dominio global de superestrellas."}
        ],
        "rules_and_tactics": [
            {"title": "Reloj de Posesión", "desc": "24 segundos para efectuar un lanzamiento al aro en cada ataque ofensivo."},
            {"title": "Altura del Aro", "desc": "Colocado exactamente a 3.05 metros de altura sobre una duela de madera pulida."}
        ],
        "leagues_and_nations": ["NBA (Estados Unidos)", "WNBA (Femenina)", "EuroLeague & FIBA World Cup"],
        "teams_and_franchises": [
            "Boston Celtics &mdash; 18 Títulos NBA",
            "Los Angeles Lakers &mdash; 17 Títulos NBA",
            "Chicago Bulls &mdash; Dinastía de los 90"
        ],
        "legends": [
            {"name": "Michael Jordan", "nickname": "Air Jordan", "country": "EE.UU.", "stat": "6 Títulos NBA & 6 MVPs", "bio": "El estándar supremo de la competitividad y el vuelo en la historia del baloncesto."},
            {"name": "LeBron James", "nickname": "The King", "country": "EE.UU.", "stat": "Máximo Anotador Histórico NBA", "bio": "Longevidad y dominio físico absoluto durante más de dos décadas."},
            {"name": "Kobe Bryant", "nickname": "Black Mamba", "country": "EE.UU.", "stat": "5 Anillos & 81 Pts en 1 Partido", "bio": "Creador de la implacable 'Mamba Mentality'."}
        ]
    },
    "atletismo": {
        "id": "atletismo",
        "name": "Atletismo",
        "category": "Verano",
        "tagline": "El deporte matriz de la humanidad: Citius, Altius, Fortius en carreras, saltos y lanzamientos.",
        "primary_color": "#ffaa00",
        "secondary_color": "#ff0055",
        "icon_symbol": "🏃‍♂️",
        "history_long": """El atletismo es la forma organizada de deporte más antigua de la historia humana, con registros de competencias de carrera pedestre que datan de los antiguos Juegos Olímpicos de la Antigua Grecia en el año 776 a.C. Es considerado con justicia el deporte matriz de la civilización: mide las capacidades físicas primarias e inalterables del ser humano.

Dividido en grandes bloques (velocidad pura, fondo y medio fondo, vallas, saltos de altura/longitud y lanzamientos de peso/jabalina), el atletismo consagra a los atletas más veloces y resistentes del planeta. La rivalidad histórica entre naciones, la pureza del cronómetro y los récords mundiales inquebrantables definen la gloria olímpica moderna.""",
        "timeline": [
            {"era": "Juegos Olímpicos Antiguos (776 a.C. - 393 d.C.)", "icon": "🏛️", "desc": "Nacimiento de la prueba fundacional del Stadion (carrera de velocidad) en Olimpia."},
            {"era": "Renacimiento Olímpico Moderno (1896 - 1980)", "icon": "🏅", "desc": "Fundación de la IAAF (World Athletics) y celebración de los primeros Juegos Olímpicos modernos en Atenas 1896."},
            {"era": "La Era de los Superhumanos (1980 - 2026)", "icon": "⚡", "desc": "Récords estratosféricos en velocidad con leyendas como Usain Bolt, pistas de tartán sintético y tecnología biomecánica avanzada."}
        ],
        "rules_and_tactics": [
            {"title": "Salidas en Velocidad", "desc": "Uso de tacos de salida en pruebas de velocidad. Cualquier salida en falso anterior al disparo del juez sanciona descalificación inmediata."},
            {"title": "Categorías de Pruebas", "desc": "Velocidad (100m, 200m, 400m), Medio fondo/Fondo (800m a Maratón), Saltos (Pértiga, Altura, Longitud) y Lanzamientos (Peso, Disco, Jabalina, Martillo)."}
        ],
        "leagues_and_nations": [
            "World Athletics (Federación Internacional de Atletismo)",
            "Diamond League (Circuito Mundial de Mitines de Élite)",
            "Potencias Mundiales: Jamaica, Estados Unidos, Kenia, Etiopía, Gran Bretaña"
        ],
        "teams_and_franchises": [
            "Selección de Jamaica (Dominio histórico en pruebas de velocidad corta)",
            "Federación de Kenia (Dinastía inalcanzable en maratones y medio fondo)"
        ],
        "legends": [
            {"name": "Usain Bolt", "nickname": "Lightning Bolt", "country": "Jamaica", "stat": "9.58s (100m) & 8 Oros Olímpicos", "bio": "El hombre más rápido de la historia de la humanidad, leyenda inigualable del tartán olímpico."},
            {"name": "Eliud Kipchoge", "nickname": "The Philosopher King", "country": "Kenia", "stat": "Sub-2 horas en Maratón & 2 Oros Ol.", "bio": "El maratonista más grande de todos los tiempos y símbolo mundial de la resistencia humana."},
            {"name": "Carl Lewis", "nickname": "King Carl", "country": "EE.UU.", "stat": "9 Medallas de Oro Olímpicas", "bio": "Dominador absoluto multiprueba en velocidad y salto de longitud durante las décadas de 1980 y 1990."},
            {"name": "Sydney McLaughlin-Levrone", "nickname": "Queen of Hurdles", "country": "EE.UU.", "stat": "Récord Mundial en 400m Vallas", "bio": "Atleta generacional con múltiples récords mundiales consecutivos y técnica biomecánica perfecta."}
        ]
    },
    "league-of-legends": {
        "id": "league-of-legends",
        "name": "League of Legends",
        "category": "eSports",
        "tagline": "El coliseo digital definitivo: estrategia en equipo de 5v5, reflejos cibernéticos y batallas en la Grieta.",
        "primary_color": "#0099ff",
        "secondary_color": "#00ffcc",
        "icon_symbol": "⚔️",
        "history_long": """Lanzado por Riot Games en 2009, League of Legends (LoL) revolucionó el entretenimiento interactivo hasta convertirse en el deporte electrónico (eSport) más seguido del planeta. El Campeonato Mundial (Worlds) llena estadios de fútbol tradicionales en todo el mundo con decenas de millones de espectadores simultáneos.

Enfrenta a dos equipos de cinco jugadores en el mapa de la Grieta del Invocador. La victoria exige una coordinación sinfónica milimétrica, control de objetivos estratégicos (Dragones y Barón Nashor), gestión de oro y reflejos cognitivos de velocidad sobrehumana.""",
        "timeline": [
            {"era": "Génesis y Worlds (2009 - 2013)", "icon": "📜", "desc": "Lanzamiento y consolidación del primer Campeonato Mundial con Fnatic y Taipei Assassins."},
            {"era": "Dinastía Coreana y T1 (2013 - 2020)", "icon": "👑", "desc": "Dominio de la LCK coreana y surgimiento de Faker conquistando múltiples Copas del Invocador."},
            {"era": "Ecosistema Global y Récords (2020 - 2026)", "icon": "⚡", "desc": "Creación de ligas regionales profesionalizadas (LCK, LPL, LEC, LTA) y estadios mundiales masivos."}
        ],
        "rules_and_tactics": [
            {"title": "Fase de Draft", "desc": "Estrategia previa donde se bloquean y eligen campeones para construir sinergias."},
            {"title": "Control de Objetivos", "desc": "Disputa constante de monstruos épicos como el Dragón y el Barón Nashor."}
        ],
        "leagues_and_nations": ["LCK (Corea - Región dominante)", "LPL (China)", "LEC (EMEA) & LTA (América)"],
        "teams_and_franchises": ["T1 &mdash; 4 Títulos Mundiales", "Gen.G &mdash; Dinastía internacional"],
        "legends": [
            {"name": "Faker (Lee Sang-hyeok)", "nickname": "Unkillable Demon King", "country": "Corea del Sur", "stat": "4 Títulos Mundiales (Worlds GOAT)", "bio": "El atleta de eSports más grande e influyente de la historia, el GOAT absoluto de LoL."},
            {"name": "Ruler (Park Jae-hyuk)", "nickname": "The Executioner", "country": "Corea del Sur", "stat": "Campeón Mundial & MVP", "bio": "Uno de los tiradores (ADC) más precisos y letales en las peleas por equipo."}
        ]
    },
    "fortnite-esports": {
        "id": "fortnite-esports",
        "name": "Fortnite Competitive",
        "category": "eSports",
        "tagline": "Battle Royale de supervivencia extrema: construcción en milisegundos y tensión en la tormenta.",
        "primary_color": "#9b51e0",
        "secondary_color": "#00f2fe",
        "icon_symbol": "🎯",
        "history_long": """Desarrollado por Epic Games en 2017, Fortnite transformó la cultura pop global y estableció un paradigma en los eSports con su mecánica de construcción y edición de estructuras en tiempo real. 

El circuito competitivo de la FNCS enfrenta a los mejores jugadores del mundo en arenas masivas donde 100 competidores luchan por sobrevivir al colapso de la tormenta con reflejos mecánicos y toma de decisiones geométrica instantánea.""",
        "timeline": [
            {"era": "Fenómeno Battle Royale (2017 - 2018)", "icon": "📜", "desc": "Lanzamiento y primeros torneos de exhibición con creadores de contenido."},
            {"era": "Copa Mundial de Nueva York (2019)", "icon": "🏟️", "desc": "Torneo histórico en el Estadio Arthur Ashe con premios multimillonarios."},
            {"era": "Era FNCS y Ligas Globales (2020 - 2026)", "icon": "⚡", "desc": "Formato estructurado de FNCS regionales y presenciales mundiales masivos."}
        ],
        "rules_and_tactics": [
            {"title": "Construcción", "desc": "Uso de materiales para levantar coberturas instantáneas y rampas en milisegundos."},
            {"title": "Rotación de Tormenta", "desc": "Planificación estratégica del desplazamiento ante el cierre del mapa circular."}
        ],
        "leagues_and_nations": ["FNCS (Circuito Global Oficial)", "Global Championship Epic Games", "Potencias: NA, EU, BR"],
        "teams_and_franchises": ["Sentinels", "Fnatic eSports"],
        "legends": [
            {"name": "Bugha (Kyle Giersdorf)", "nickname": "Solos World Champion", "country": "EE.UU.", "stat": "Campeón Mundial Solo 2019", "bio": "Dominó la Copa Mundial con una superioridad mecánica que cambió el estándar competitivo."},
            {"name": "TaySon (Tai Starčič)", "nickname": "EU King", "country": "Eslovenia", "stat": "Campeón Múltiple FNCS Europa", "bio": "Considerado el jugador más cerebral e inteligente de la región europea."}
        ]
    },
    "ea-sports-fc": {
        "id": "ea-sports-fc",
        "name": "EA Sports FC / FIFA eSports",
        "category": "eSports",
        "tagline": "El simulador de fútbol virtual definitivo: Ultimate Team, eChampions League y gloria global en la consola.",
        "primary_color": "#00e5ff",
        "secondary_color": "#7000ff",
        "icon_symbol": "🎮",
        "history_long": """La saga de simulación futbolística de EA Sports (anteriormente FIFA y actualmente EA Sports FC) es el videojuego deportivo más influyente de la historia. El circuito competitivo profesional de esports reúne a los mejores creadores de jugadas tácticas del mundo en torneos oficiales como la eChampions League y la FIFAe World Cup.

Los jugadores profesionales controlan plantillas virtuales de máxima categoría con una lectura ultrarrápida del motor de física del juego, combinando habilidades de regate avanzado, defensa milimétrica en zonas de presión y definición clínica ante la portería virtual.""",
        "timeline": [
            {"era": "Inicios de la Franquicia (1993 - 2010)", "icon": "📜", "desc": "Lanzamiento de los primeros simuladores de fútbol en perspectiva isométrica y 3D."},
            {"era": "La Explosión de Ultimate Team (2010 - 2020)", "icon": "⚽", "desc": "Nacimiento del modo coleccionable Ultimate Team y primeros torneos mundiales oficiales de esports."},
            {"era": "Rebranding EA Sports FC y eChampions League (2020 - 2026)", "icon": "⚡", "desc": "Consolidación de ligas virtuales de clubes de fútbol real (ePremier League, eLaLiga) y transmisiones globales de eChampions League."}
        ],
        "rules_and_tactics": [
            {"title": "Gestión de Ultimate Team", "desc": "Construcción táctica de plantillas de ensueño combinando química de jugadores y formaciones."},
            {"title": "Mecánicas de Precisión", "desc": "Uso de tiros de calidad con tiempo, regates dirigidos y presión asertiva con doble marcaje."}
        ],
        "leagues_and_nations": ["eChampions League", "ePremier League & eLaLiga Oficial", "FIFAe World Cup"],
        "teams_and_franchises": ["Manchester City eSports", "PSG Esports", "Ajax eSports"],
        "legends": [
            {"name": "Msdossary (Mosaad Aldossary)", "nickname": "The Champion", "country": "Arabia Saudita", "stat": "Campeón Mundial FIFAe", "bio": "Uno de los competidores virtuales más dominantes, estables y respetados en la historia del simulador."},
            {"name": "Tekkz (Mossad / Donovan)", "nickname": "Wonderkid", "country": "Reino Unido", "stat": "Múltiples Títulos de Majors", "bio": "Famoso por su estilo de juego ultra ofensivo y dominio aplastante en múltiples torneos internacionales."}
        ]
    }
}