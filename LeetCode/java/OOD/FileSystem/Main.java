// package LeetCode.java.OOD.FileSystem;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
  public static void main(String[] args) {
    new Main().test();
  }
  
  private void test() {
    SearchParams params = new SearchParams();
    params.extension = "xml";
    params.minSize = 2;
    params.maxSize = 100;

    File xmlFile = new File();
    xmlFile.setContent("aaa.xml".getBytes());
    xmlFile.name = "aaa.xml";

    File txtFile = new File();
    txtFile.setContent("bbb.txt".getBytes());
    txtFile.name = "bbb.txt";

    File jsonFile = new File();
    jsonFile.setContent("ccc.json".getBytes());
    jsonFile.name = "ccc.json";

    Directory dir1 = new Directory();
    dir1.addEntry(txtFile);
    dir1.addEntry(xmlFile);

    Directory dir0 = new Directory();
    dir0.addEntry(jsonFile);
    dir0.addEntry(dir1);

    FileSearcher searcher = new FileSearcher();
    System.out.println(searcher.search(dir0, params));
  }

  public interface IEntry {

    String getName();

    void setName(String name);

    int getSize();

    boolean isDirectory();
  }

  private abstract class Entry implements IEntry {
    protected String name;

    @Override
    public String getName() {
      return name;
    }

    @Override
    public void setName(String name) {
      this.name = name;
    }
    
  }

  public class File extends Entry {
    private byte[] content;

    public String getExtension() {
      return name.substring(name.indexOf(".") + 1);
    }

    public void setContent(byte[] content) {
      this.content = content;
    }

    public byte[] getContent() {
      return content;
    }

    @Override
    public int getSize() {
      return content.length;
    }

    @Override
    public boolean isDirectory() {
      return false;
    }
    
    @Override
    public String toString() {
      return "File{" +
        "name='" + name + '\'' +
        '}';
    }
  }

  public class Directory extends Entry {
	  private List<Entry> entries = new ArrayList<>();

    @Override
    public int getSize() {
      int size = 0;
      for (Entry entry  : entries) {
        size += entry.getSize();
      }

      return size;
    }

    @Override
    public boolean isDirectory() {
      return true;
    }

    public void addEntry(Entry entry) {
      this.entries.add(entry);
    }
  }

  public class SearchParams {
    String extension;
    Integer minSize;
    Integer maxSize;
    String name;
  }

  public interface IFilter {

	  boolean isValid(SearchParams params, File file);

  }

  public class ExtensionFilter implements IFilter {

    @Override
    public boolean isValid(SearchParams params, File file) {
      if (params.extension == null) {
        return true;
      }

      return file.getExtension().equals(params.extension);
    }

  }

  public class MinSizeFilter implements IFilter {

    @Override
    public boolean isValid(SearchParams params, File file) {
      if (params.minSize == null) {
        return true;
      }

      return file.getSize() >= params.minSize;
    }

  }

  public class MaxSizeFilter implements IFilter {

    @Override
    public boolean isValid(SearchParams params, File file) {
      if (params.maxSize == null) {
        return true;
      }

      return file.getSize() <= params.maxSize;
    }

  }

  public class NameFilter implements IFilter {

    @Override
    public boolean isValid(SearchParams params, File file) {
      if (params.name == null) {
      return true;
      }

      return file.getName().equals(params.name);
    }

  }

  public class FileFilter {
    private final List<IFilter> filters = new ArrayList<>();

    public FileFilter() {
      filters.add(new NameFilter());
      filters.add(new MaxSizeFilter());
      filters.add(new MinSizeFilter());
      filters.add(new ExtensionFilter());
    }

    public boolean isValid(SearchParams params, File file) {
      for (IFilter filter : filters) {
        if (!filter.isValid(params, file)) {
          return false;
        }
      }

      return true;
    }

  }

  public class FileSearcher {
    private FileFilter filter = new FileFilter();

    public List<File> search(Directory dir, SearchParams params) {
      List<File> files = new ArrayList<>();

      Queue<Directory> queue = new LinkedList<>();
      queue.add(dir);

      while (!queue.isEmpty()) {
        Directory folder = queue.poll();

        for (IEntry entry : folder.entries) {
          if (entry.isDirectory()) {
          queue.add((Directory) entry);
          } else {
          File file = (File) entry;
          if (filter.isValid(params, file)) {
            files.add(file);
          }
          }
        }
      }

      return files;
	  }
  }
    
}




// public class FileSystemDesign {

//   // ===== Interface =====
//   interface IEntry {
//     String getName();
//     void setName(String name);
//     int getSize();
//     boolean isDirectory();
//   }

//   // ===== Abstract Class =====
//   abstract class Entry implements IEntry {
//     String name;
//   }

//   // ===== File =====
//   class File extends Entry {
//     byte[] content;

//     void setContent(byte[] data);
//     byte[] getContent();
//     String getExtension();
//     int getSize();              // content.length
//     boolean isDirectory();      // return false
//   }

//   // ===== Directory =====
//   class Directory extends Entry {
//     List<Entry> entries;

//     void addEntry(Entry e);
//     List<Entry> getEntries();
//     int getSize();              // sum of child sizes
//     boolean isDirectory();      // return true
//   }

//   // ===== Search Parameters =====
//   class SearchParams {
//     String name;
//     String extension;
//     Integer minSize;
//     Integer maxSize;
//   }

//   // ===== Filter Interface =====
//   interface IFilter {
//     boolean isValid(SearchParams params, File file);
//   }

//   // ===== Concrete Filters =====
//   class NameFilter implements IFilter {
//     boolean isValid(SearchParams params, File file);
//   }

//   class ExtensionFilter implements IFilter {
//     boolean isValid(SearchParams params, File file);
//   }

//   class MinSizeFilter implements IFilter {
//     boolean isValid(SearchParams params, File file);
//   }

//   class MaxSizeFilter implements IFilter {
//     boolean isValid(SearchParams params, File file);
//   }

//   // ===== Filter Aggregator =====
//   class FileFilter {
//     List<IFilter> filters;

//     FileFilter();  // register all filters
//     boolean isValid(SearchParams params, File file);
//   }

//   // ===== File Searcher =====
//   class FileSearcher {
//     FileFilter filter;

//     List<File> search(Directory root, SearchParams params); // BFS traversal
//   }
// }
