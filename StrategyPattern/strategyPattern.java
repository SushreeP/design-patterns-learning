public interface FlyBehaviour{
    void fly();
}

public class FlyWithWings implements FlyBehaviour{
    public void fly(){
        System.out.println("I'm flying!");
    }
}

public class FlyNoWay implements FlyBehaviour{
    public void fly(){
        System.out.println("I can't fly!");
    }
}

public interface QuackBehaviour{
    void quack();
}

public class Quack implements QuackBehaviour{
    public void quack(){
        System.out.println("I can quack.");
    }
}

public class Squeak implements QuackBehaviour{
    public void quack(){
        System.out.println("I can squeak.");
    }
}

public class Mute implements QuackBehaviour{
    public void quack(){
        System.out.println("I am a silent duck.");
    }
}

public abstract class Duck{
    FlyBehaviour flyBehaviour;
    QuackBehaviour quackBehaviour;

    abstract void display();
    public void performFly(){
        flyBehaviour.fly();
    }

    public void performQuack(){
        quackBehaviour.quack();
    }

    public void swim (){
        System.out.println("All ducks can swim.So I can too.");
    }
}

public class MallardDuck extends Duck{

    public MallardDuck(){
        quackBehaviour = new Quack();
        flyBehaviour = new FlyWithWings();
    }

    public void display(){
        System.out.println("I'm a  Mallard Duck.")
    }

}

public class MiniDuckSimulator{
    public static void main(String[] args){
        Duck mallard = new MallardDuck();
        mallard.performFly();
        mallard.performQuack();
        mallard.display();
    }
}