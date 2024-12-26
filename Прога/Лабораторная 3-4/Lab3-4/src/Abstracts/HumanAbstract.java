package Abstracts;


import Interfaces.Job;

public abstract class HumanAbstract implements Job {
    private final String name;

    public void walkAround(PlaceAbstract place) {
        place.show();
    }
    public PlaceAbstract createPlace(PlaceAbstract place) {
        return place;
    }
    @Override
    public void doJob(HumanAbstract human, PlaceAbstract place) {
        System.out.println(human.getName() + " выполняет работу в " + place.getPlaceName());
    }
    public HumanAbstract(String name, int age) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
    @Override
    public String toString() {
        return "Человек по имени " + name;
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getName().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (getClass() != obj.getClass())
            return false;
        return obj.hashCode() == this.hashCode();
    }
}
