package Classes;

import Enums.Places;

public record Attribute(Places place, String value) {
    public String getValue() {
        return value;
    }
}
