import Abstracts.PlaceAbstract;
import Classes.Actors.Goat;
import Classes.Actors.Gulliver;
import Classes.Attribute;
import Classes.Condition;
import Classes.Place;
import Enums.Places;
import Exceptions.AcresException;
import Exceptions.AgeException;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            //subjects
            Gulliver gulliver = new Gulliver(44);
            Goat goatMale = new Goat(Goat.Gender.MALE);
            Goat goatFemale = new Goat(Goat.Gender.FEMALE);

            //locations
            PlaceAbstract island = new Place(Places.Island.getPlace());
            island.setAttributes(List.of(new Attribute(Places.Island, "отыскивая самые глухие места")));
            PlaceAbstract corner = new Place(Places.Corner.getPlace());
            corner.setAttributes(List.of(new Attribute(Places.Corner, "хорошо укрытый от нескромных взоров")));
            PlaceAbstract lawn = new Place(Places.Lawn.getPlace());
            lawn.setAttributes(List.of(new Attribute(Places.Lawn, "небольшая в низине")));
            PlaceAbstract thicket = new Place(Places.Thicket.getPlace());
            thicket.setAttributes(List.of(new Attribute(Places.Thicket, "укрытая в чаще леса")));
            PlaceAbstract forest = new Place(Places.Forest.getPlace());
            forest.setAttributes(List.of(new Attribute(Places.Forest, "который обступал полянку")));
            PlaceAbstract home = new Place(Places.Home.getPlace());
            home.setAttributes(List.of(new Attribute(Places.Home, "с восточной части")));
            PlaceAbstract fence = new Place(Places.Fence.getPlace());
            fence.setAttributes(List.of(new Attribute(Places.Fence, "не торопясь, очень медленно")));
            PlaceAbstract paddock = new Place(Places.Paddock.getPlace());
            paddock.setAttributes(List.of(new Attribute(Places.Paddock, "который был плотно огорожен")));

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
            gulliver.addLocation(island);
            gulliver.walk(island);
            conditions[0].printName();
            gulliver.addLocation(corner);
            gulliver.walk(corner);
            gulliver.happiness();
            gulliver.addLocation(lawn);
            gulliver.walk(lawn);
            gulliver.walk(thicket);
            gulliver.lost(thicket, home, island);
            gulliver.walk(home);
            gulliver.size(lawn);
            gulliver.addLocation(forest);
            gulliver.walk(forest);
            gulliver.addLocation(paddock);
            gulliver.worked();
            conditions[1].printName();
            gulliver.someWorkWithNewPlace(paddock);
            gulliver.walk(paddock);
            gulliver.putted(paddock, goatMale, goatFemale);
            conditions[2].printName();
            goatMale.accustomed(paddock, gulliver);
            goatFemale.accustomed(paddock, gulliver);
            goatMale.lost();
            goatFemale.lost();
            gulliver.separated(goatMale, goatFemale, paddock);
            conditions[3].printName();
            gulliver.someWorkWithNewPlace(fence);
            gulliver.walk(fence);
            System.out.println();
        }
        catch (AcresException | AgeException ex) {
            System.out.println(ex.getMessage());
        }
    }
}