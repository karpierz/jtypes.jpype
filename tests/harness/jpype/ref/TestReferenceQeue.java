package jpype.ref;

//<AK> added - import from jt.jtypes
//import com.jt.ref.ReferenceQueue;
//import com.jt.ref.Reference;
//</AK>

public class TestReferenceQeue
{
  public static void main(String[] args)
  {
//    final ReferenceQueue queue = new ReferenceQueue(); //<AK> was: JPypeReferenceQueue
//    
//    new Thread(new Runnable() {
//
//      public void run()
//      {
//        queue.start(); //<AK> was: queue.startManaging();
//      }
//      
//    }).start();
//    
//    Object dummy = new Object();
//    long dummyAddress = 123456;
//    
//    Reference ref = new Reference(dummy, queue); //<AK> was: JPypeReference
//    
//    queue.registerReference(ref, dummyAddress);  //<AK> was: queue.registerRef
//    
//    System.out.println("ref is enqueued? "+ref.isEnqueued());
//    
//    long start = System.currentTimeMillis();
//    dummy = null;
//    while (System.currentTimeMillis()-start < 30000 && ! (ref.isEnqueued()))
//    {
//      System.gc();
//      System.out.print(".");
//      try
//      {
//        Thread.sleep(250);
//      }
//      catch(InterruptedException ex) {}
//    }
//    
//    System.out.println();
//    System.out.println("ref is enqueued? "+ref.isEnqueued());
//    queue.stop();
  }
}
