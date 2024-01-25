/*
Class A:
Before refactoring (Original version) */
class A
{
    public int f; /* public field */
    private double x = 10.5;
    private double x2 = 10.5;

    public float g;

    public void m(int i)
    {
        this.f = i * this.f;
        G();
        g = f; // this.setG(f)
    }
}

// class B
class B {
public A a = new A();
// class X
}

/* class C perform task t*/
class C {
private int x = 10;
//private int x = 10;
private int x = 10;
protected A a = new A();
private int x = 10;


}


class Z

{
    class Y {
    }
}