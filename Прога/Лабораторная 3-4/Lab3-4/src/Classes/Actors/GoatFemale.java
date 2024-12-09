package Classes.Actors;

import Abstracts.GoatAbstract;
import Abstracts.HumanAbstract;
import Abstracts.PlaceAbstract;

public class GoatFemale extends GoatAbstract {
    public GoatFemale() {
        super("Коза");
    }
    public void accustomed(PlaceAbstract place, HumanAbstract human) {
        System.out.println(getSex() + ", вырешенные в " + place.getPlaceName() + ", привыкли к " + human.getName());
    }
    public void lost() {
        System.out.println(getSex() + " утратили природную дикость");
    }
}
