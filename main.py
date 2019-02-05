app = webapp2.WSGIApplication(
    [("/blog", BlogMainHandler),
     ("/blog/newpost", BlogNewPostHandler),
     ('/blog/post/(\d+)', BlogPostViewHandler),
     ],
    debug=True)
