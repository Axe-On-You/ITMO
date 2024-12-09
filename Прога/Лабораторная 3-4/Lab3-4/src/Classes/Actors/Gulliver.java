package Classes.Actors;

import Abstracts.GoatAbstract;
import Abstracts.HumanAbstract;
import Abstracts.PlaceAbstract;
import Exceptions.AcresException;
import Exceptions.AgeException;

import java.util.Random;

public class Gulliver extends HumanAbstract {
    public Gulliver(int age) throws AgeException{
        super("Гулливер", age);
        if (age > 50 || age < 30) throw new AgeException("в оригинальной истории Гулливеру было около 40 лет.");
    }
    public void went(PlaceAbstract place) {
        System.out.println(getName() + " исходил весь " + place.getPlaceName());
    }
    public void chose(PlaceAbstract place) {
        System.out.println(getName() + " выбрал один " + place.getPlaceName());
        System.out.println(place.getPlaceName() + " был хорошо укрыт от нескромных взоров");
    }
    public void happiness() {
        System.out.println(getName() + " не мог желать большего");
    }
    public void lawn(PlaceAbstract place1, PlaceAbstract place2) {
        System.out.println(place1.getPlaceName() + " была " + place2.getPlaceName());
    }
    public void lost(PlaceAbstract place1, PlaceAbstract place2, PlaceAbstract place3) {
        System.out.println(getName() + " заблудился " + place1.getPlaceName() + ", когда возвращался " + place2.getPlaceName() + " с " + place3.getPlaceName());
    }
    public void size(PlaceAbstract place) {
        Random random = new Random();
        int acresChance = random.nextInt(0, 3);
        System.out.println(place.getPlaceName() + " занимала около " + acresChance + " акров");
        if (acresChance < 1) throw new AcresException(acresChance, "акров");
    }
    public void forest(PlaceAbstract place1, PlaceAbstract place2, PlaceAbstract place3) {
        System.out.println(place1.getPlaceName() + " обступал " + place2.getPlaceName() + ", образуя " + place3.getPlaceName());
    }
    public void worked() {
        System.out.println(getName() + " принялся за работу");
    }
    public void putted(PlaceAbstract place, GoatAbstract goat1, GoatAbstract goat2){
        System.out.println(getName() + " завел в " + place.getPlaceName() + " " + goat1.getSex() + " и " + goat2.getSex());
    }
    public void separated(GoatAbstract goat1, GoatAbstract goat2, PlaceAbstract place) {
        System.out.println(getName() + " отделил несколько " + goat1.getSex() + " и " + goat2.getSex() + ", отвел их в " + place.getPlaceName());
    }
    public void reinforced(PlaceAbstract place) {
        System.out.println(getName() + " укрепил " + place.getPlaceName() + " очень медленно, не торопясь");
    }
}
