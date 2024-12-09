import Abstracts.PlaceAbstract;
import Classes.Actors.GoatFemale;
import Classes.Actors.GoatMale;
import Classes.Actors.Gulliver;
import Classes.Condition;
import Classes.Place;
import Enums.Places;
import Exceptions.AcresException;
import Exceptions.AgeException;

public class Main {
    public static void main(String[] args) {
        try {
            //subjects
            Gulliver gulliver = new Gulliver(44);
            GoatMale goat1 = new GoatMale();
            GoatFemale goat2 = new GoatFemale();

            //locations
            PlaceAbstract island = new Place(Places.Island.getPlace());
            PlaceAbstract corner = new Place(Places.Corner.getPlace());
            PlaceAbstract lawn = new Place(Places.Lawn.getPlace());
            PlaceAbstract thicket = new Place(Places.Thicket.getPlace());
            PlaceAbstract forest = new Place(Places.Forest.getPlace());
            PlaceAbstract home = new Place(Places.Home.getPlace());
            PlaceAbstract fence = new Place(Places.Fence.getPlace());
            PlaceAbstract paddock = new Place(Places.Paddock.getPlace());

            //some conditions
            Condition[] conditions = new Condition[4];
            conditions[0] = new Condition("Наконец");
            conditions[1] = new Condition("Спустя четыре недели");
            conditions[2] = new Condition("Теперь это не представляло большого труда");
            conditions[3] = new Condition("Еще некоторое время спустя");

            System.out.println("Initialization is over");
            System.out.println();
            System.out.println();
            System.out.println();


            //text
            gulliver.went(island);
            conditions[0].printName();
            gulliver.chose(corner);
            gulliver.happiness();
            gulliver.lawn(lawn, thicket);
            gulliver.lost(thicket, home, island);
            gulliver.size(lawn);
            gulliver.forest(forest, lawn, fence);
            gulliver.worked();
            conditions[1].printName();
            gulliver.putted(paddock, goat1, goat2);
            conditions[2].printName();
            goat1.accustomed(paddock, gulliver);
            goat2.accustomed(paddock, gulliver);
            goat1.lost();
            goat2.lost();
            gulliver.separated(goat1, goat2, paddock);
            conditions[3].printName();
            gulliver.reinforced(paddock);
            System.out.println();
        }
        catch (AcresException | AgeException ex) {
            System.out.println(ex.getMessage());
        }
    }
}