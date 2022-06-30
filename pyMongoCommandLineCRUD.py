from select import select
from venv import create
import pymongo
import datetime
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection
posts = db.posts

def createPost(posts):
  print("\nCreate Post")
  authorFirstName = input("Enter author first name: ")
  authorLastName =  input("Enter author last name: ")
  postTitle = input("Enter post title: ")
  postBody = input("Enter post body: ")
  
  post = {"author first name": authorFirstName, "author last name": authorLastName, "title": postTitle, "text": postBody, "date": datetime.datetime.utcnow()}
  
  print(post)
  post_id = posts.insert_one(post).inserted_id

  print("Post successful!")

def readPost(posts):
  print("\nRead")
  print("1 - Read by author first name")
  print("2 - Read by author last name")
  print("3 - Read by post title")
  print("4 - Exit Read")

  readChoice = input("Enter a selection: ")
  
  while readChoice != "4":
    if readChoice == "1":
      authorFirstName = input("Enter author first name: ")
      cursor = posts.find({"author first name": authorFirstName})
      selectedPosts = []
      selectedPostIDs = []
      for post in cursor:
        selectedPosts.append(post)
        selectedPostIDs.append(post["_id"])
      
      if len(selectedPosts) > 1:
        viewPosts = ""
        while ((viewPosts != "Y") or (viewPosts != "n")):
          viewPosts = "n"
          viewPosts = input("Your query returned more than one post. Would you like to view the posts [Y/n]?")
          if viewPosts == "Y":
            for post in selectedPosts:
              print("\n")
              pprint.pprint(post)
          else:
            break
          break
        print("\n")
        for ID in selectedPostIDs:
          print(ID)
      else:
        pprint.pprint(selectedPosts)
      break
    elif readChoice == "2":
      authorLastName = input("Enter author last name: ")
      cursor = posts.find({"author last name": authorLastName})
      selectedPosts = []
      selectedPostIDs = []
      for post in cursor:
        selectedPosts.append(post)
        selectedPostIDs.append(post["_id"])
      
      if len(selectedPosts) > 1:
        viewPosts = ""
        while ((viewPosts != "Y") or (viewPosts != "n")):
          viewPosts = "n"
          viewPosts = input("Your query returned more than one post. Would you like to view the posts [Y/n]?")
          if viewPosts == "Y":
            for post in selectedPosts:
              print("\n")
              pprint.pprint(post)
          else:
            break
          break
        print("\n")
        for ID in selectedPostIDs:
          print(ID)
      else:
        pprint.pprint(selectedPosts)
      break
    elif readChoice == "3":
      postTitle = input("Enter post title: ")
      cursor = posts.find({"title": postTitle})
      selectedPosts = []
      selectedPostIDs = []
      for post in cursor:
        selectedPosts.append(post)
        selectedPostIDs.append(post["_id"])
      
      if len(selectedPosts) > 1:
        viewPosts = ""
        while ((viewPosts != "Y") or (viewPosts != "n")):
          viewPosts = "n"
          viewPosts = input("Your query returned more than one post. Would you like to view the posts [Y/n]?")
          if viewPosts == "Y":
            for post in selectedPosts:
              print("\n")
              pprint.pprint(post)
          else:
            break
          break
        print("\n")
        for ID in selectedPostIDs:
          print(ID)
      else:
        pprint.pprint(selectedPosts)
      break
    elif readChoice == "4":
      break
    else:
      break
    
def updatePost(posts):
  print("\nUpdate")
    
  print("1 - Update by author first name")
  print("2 - Update by author last name")
  print("3 - Update by post title")
  print("4 - Exit Update")

  updateChoice = input("Enter a selection: ")
  
  while updateChoice != "4":
    if updateChoice == "1":
      authorFirstName = input("Enter author first name: ")
      post = posts.find({"author first name": authorFirstName})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    if updateChoice == "2":
      authorLastName = input("Enter author last name: ")
      post = posts.find({"author last name": authorLastName})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    if updateChoice == "3":
      postTitle = input("Enter post title: ")
      post = posts.find({"title": postTitle})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    elif updateChoice == "4":
      break
    
def updateByPostID(post, post_id):
  
  updatePost = ""
  while ((updatePost != "Y") or (updatePost != "n")):
    updatePost = "n"
    updatePost = input("Update this post [Y/n]? Default is [n].")
    if updatePost == "n":
      break
    else:
      print("1 - Update author first name")
      print("2 - Update author last name")
      print("3 - Update post title")
      print("4 - Update post body")
      print("5 - Exit Update")
      
      selection = input("Enter a selection: ")
      
      while selection != "5":
        if selection == "1":
          authorFirstName = input("Enter new author first name: ")
          posts.update_one({"_id": post_id}, { "$set": {"author first name": authorFirstName}})
          post = posts.find({"author first name": authorFirstName})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "2":
          authorLastName = input("Enter new author last name: ")
          posts.update_one({"_id": post_id}, { "$set": {"author last name": authorLastName}})
          post = posts.find({"author last name": authorFirstName})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "3":
          postTitle = input("Enter new post title: ")
          posts.update_one({"_id": post_id}, { "$set": {"title": postTitle}})
          post = posts.find({"title": postTitle})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "4":
          postBody = input("Enter new post body: ")
          posts.update_one({"_id": post_id}, { "$set": {"text": postBody}})
          post = posts.find({"text": postBody})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "5":
          break
      break
    break

def doStuff(db, collection, posts):
  choice = 0
  while choice != "5":
    print("\nPlease make a selection from 1 to 5:")
    print("1 - Create Post")
    print("2 - Read Post")
    print("3 - Update Post")
    print("4 - Delete Post")
    print("5 - Exit")
    
    choice = input()
    if choice == "1":
      createPost(posts)
    elif choice == "2":
      readPost(posts)
    elif choice == "3":
      updatePost(posts)
    elif choice == "4":
      print("\nDelete")
      print("1 - Delete by author first name")
      print("2 - Delete by author last name")
      print("3 - Delete by post title")
      print("4 - Exit Delete")

      readChoice = input("Enter a selection: ")
      
      while readChoice != "4":
        if readChoice == "1":
          authorFirstName = input("Enter author first name: ")
          post = posts.find({"author first name": authorFirstName})
          pprint.pprint(post[0])
          delete = "n"
          delete = input("Delete this post [Y/n]? ")
          if delete == "Y":
            posts.delete_one({"_id": post["_id"]})
          else:
            break
          break
        if readChoice == "2":
          authorLastName = input("Enter author last name: ")
          post = posts.find({"author last name": authorLastName})
          pprint.pprint(post[0])
          delete = "n"
          delete = input("Delete this post [Y/n]? ")
          if delete == "Y":
            posts.delete_one({"_id": post["_id"]})
          else:
            break
          break
        if readChoice == "3":
          postTitle = input("Enter post title: ")
          post = posts.find({"title": postTitle})
          pprint.pprint(post)
          delete = "n"
          delete = input("Delete this post [Y/n]? ")
          if delete == "Y":
            posts.delete_one({"_id": post["_id"]})
          break
        elif readChoice == "4":
          break
        elif choice == "5":
          print("\nExit")
          dropDatabase = "n"
          dropDatabase = input("Drop database test_database [Y/n]? Default is [n].")
          if dropDatabase == "Y":
            client.drop_database('test_database')
          break

doStuff(db, collection, posts)