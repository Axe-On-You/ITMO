package Abstracts;


public abstract class GoatAbstract {
    public enum Gender {
        MALE("Козел"),
        FEMALE("Коза");

        private final String name;

        Gender(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    public abstract String getSex();

    @Override
    public String toString() {
        return "Коза или козел? ->" + getSex();
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getSex().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (getClass() != obj.getClass())
            return false;
        return obj.hashCode() == this.hashCode();
    }
}
