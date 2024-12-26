// lab2, var: 1118
package lab2;

import mypokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class Program {

    // https://pokemondb.net/pokedex/Spiritomb
    // https://pokemondb.net/pokedex/Bonsly
    // https://pokemondb.net/pokedex/Sudowoodo
    // https://pokemondb.net/pokedex/Slakoth
    // https://pokemondb.net/pokedex/Vigoroth
    // https://pokemondb.net/pokedex/Slaking

    public static void main(String[] args) {

        Battle b = new Battle();

        Spiritomb spiritomb = new Spiritomb("ИТМО", 1);
        Bonsly bonsly = new Bonsly("СППО", 1);
        Sudowoodo sudowoodo = new Sudowoodo("КТ", 1);
        Slakoth slakoth = new Slakoth("ИС", 1);
        Vigoroth vigoroth = new Vigoroth("ПИиКТ", 1);
        Slaking slaking = new Slaking("ВТ", 1);

        b.addAlly(bonsly);
        b.addAlly(sudowoodo);
        b.addAlly(slakoth);
        b.addAlly(vigoroth);

        b.addFoe(spiritomb);
        b.addFoe(slaking);

        b.go();
    }

    public static boolean chance(double chance) {
        return chance > Math.random();
    }   
}
