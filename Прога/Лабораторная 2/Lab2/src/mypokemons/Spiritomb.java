package mypokemons;

import mymoves.spiritomb.*;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Spiritomb extends Pokemon {

    public Spiritomb(String name, int level) {
        super(name, level);

        super.setType(Type.GHOST, Type.DARK);

        super.setStats(50, 92, 108, 92, 108, 35);

        DarkPulse darkPulse = new DarkPulse(80, 100);
        Swagger swagger = new Swagger(0, 85);
        FoulPlay foulPlay = new FoulPlay(95, 100);
        ShadowSneak shadowSneak = new ShadowSneak(40, 100, 1, 1);

        super.setMove(darkPulse, swagger, foulPlay, shadowSneak);
    }
}
