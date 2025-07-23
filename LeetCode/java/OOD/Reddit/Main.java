class Post {
  String id;
  String title;
  String content;
  List<Comment> comments;

  void addComment(Comment c);
  List<Comment> getComments();
}

class Comment {
  String id;
  String content;
  boolean deleted;
  Comment parent;
  List<Comment> replies;

  void addReply(Comment reply);
  void delete();
  int getDepth(); // Calculates depth from root
  List<Comment> getReplies();
}

class RedditService {
  int maxDepth;

  RedditService(int maxDepth);
  Post createPost(String title, String content);
  Comment addCommentToPost(Post post, String content);
  Comment replyToComment(Comment parent, String content); // throws if depth > max
  void deleteComment(Comment comment);
}
