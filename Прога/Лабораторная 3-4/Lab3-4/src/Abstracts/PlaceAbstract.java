package Abstracts;


import Interfaces.InPlace;

public abstract class PlaceAbstract implements InPlace {
    private final String placeName;

    public PlaceAbstract(String placeName){
        this.placeName = placeName;
    }
    public String getPlaceName(){
        return placeName;
    }

    @Override
    public String toString() {
        return "Место " + placeName;
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getPlaceName().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (getClass() != obj.getClass())
            return false;
        return obj.hashCode() == this.hashCode();
    }
}
