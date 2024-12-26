package Classes.Actors;

import Abstracts.GoatAbstract;
import Abstracts.HumanAbstract;
import Abstracts.PlaceAbstract;

public class Goat extends GoatAbstract {
    private final Gender gender;

    public Goat(Gender gender) {
        this.gender = gender;
    }

    @Override
    public String getSex() {
        return gender.getName(); // Return the name of the gender
    }

    public void accustomed(PlaceAbstract place, HumanAbstract human) {
        System.out.println(gender.getName() + ", вырешенные в " + place.getPlaceName() + ", привыкли к " + human.getName());
    }

    public void lost() {
        System.out.println(gender.getName() + " утратили природную дикость");
    }
}