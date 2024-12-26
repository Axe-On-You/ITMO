package Abstracts;


import Classes.Attribute;
import Interfaces.InPlace;

import java.util.List;

public abstract class PlaceAbstract implements InPlace {
    private final String placeName;
    private List<Attribute> attributes;

    public void setAttributes(List<Attribute> attributes) {
        this.attributes = attributes;
    }

    public void show() {
        for (Attribute attribute : attributes) {
            System.out.println(attribute.getValue());
        }
    }

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
