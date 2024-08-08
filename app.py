from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement
from helpers import check_endpoint_info

app = Flask(__name__)


## function to Create client

@app.post('/api/client')
def insert_client():
    valid_check = check_endpoint_info(request.json, ['name', 'email','first_name', 'last_name', 'image_url', 'username', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_client(?, ?, ?, ?, ?, ?, ?)", [request.json.get("name"), request.json.get("email"), request.json.get("first_name"), request.json.get("last_name"), request.json.get("image_url"), request.json.get("username"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    

#function to get the client

@app.get('/api/clients')
def get_clients(): 

    try: 
        results = run_statement("CALL get_clients()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    

#function to update the client  

@app.patch("/api/client")
def update_client():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_token(?)", [token])
    print(results[0]['id'])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['email', 'password'])

    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_client(?, ?, ?)", [results[0]['id'], request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify('Client info updated successfully'), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
     
 


#delete client comeback

@app.delete('/api/delete_client')
def delete_client():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_client(?,?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)







#Functions to post the client_login and delete the client_login


#function to post/create the client_login

@app.post('/api/client_login')
def post_client_login():
    valid_check = check_endpoint_info(request.json, ['email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_login(?, ?)", [ request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)



@app.delete('/api/delete_client_login')
def delete_client_login():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_client_login(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    




#Restaurant functions


@app.post('/api/restaurant')
def post_restaurant():
    valid_check = check_endpoint_info(request.json, ['name', 'address', 'phone_number', 'bio', 'city', 'banner_url', 'email', 'password', 'profile_url'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_restaurant(?, ?, ?, ?, ?, ?, ?, ?, ?)", [request.json.get("name"), request.json.get("address"), request.json.get("phone_number"), request.json.get("bio"), request.json.get("city"), request.json.get("banner_url"), request.json.get("email"), request.json.get("password"), request.json.get("profile_url")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)


#get restaurant

@app.get('/api/restaurant')
def get_restaurant(): 

    try: 
        results = run_statement("CALL get_restaurant()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)


#get restaurants

@app.get('/api/restaurants')
def get_restaurants(): 

    try: 
        results = run_statement("CALL get_restaurants()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    

@app.get('/api/restaurant')
def get_Restaurant(): 

    try: 
        results = run_statement("CALL get_restaurants()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results[0]), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    
    
    # Update restaurant
    

@app.patch("/api/restaurant")
def update_restaurant():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results[0]['id'])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['email', 'password'])

    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_restaurant(?, ?, ?)", [results[0]['id'], request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify('Client info updated successfully'), 200)
    else: 
       return make_response(jsonify("Sorry, something went wrong"), 500)
    


#Delete restaurant


@app.delete('/api/delete_restaurant')
def delete_restaurant():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_restaurant(?,?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)






#post restaurant login

@app.post('/api/restaurant_login')
def post_restaurant_login():
    valid_check = check_endpoint_info(request.json, ['email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_restaurant_login(?, ?)", [ request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    

#Delete restaurant login


@app.delete('/api/delete_restaurant_login')
def delete_restaurant_login():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_restaurant_login(?, ?)", [results[0]['id'], request.json.get("password")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)


    

#Menu Functions


    #post menu_item  comeback

@app.post('/api/menu_items')
def post_menu():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    
    valid_check = check_endpoint_info(request.json, [ 'description', 'name', 'price', 'image_url'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)

    results = run_statement("CALL post_menu(?, ?, ?, ?, ?)", [results[0]['id'], request.json.get("description"), request.json.get("name"), request.json.get("price"), request.json.get("image_url")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    


#get menu items

@app.get('/api/menu_items')
def get_menus(): 

    try: 
        results = run_statement("CALL get_menu()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    

#get menu item
    
@app.get('/api/menu')
def get_menu(): 
    try: 
        results = run_statement("CALL get_menu()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results[0]), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    

#Update menu item


@app.patch("/api/menu")
def update_menu():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results[0]['id'])
    if(len(results) == 0):
        return 'token invalid'

    valid_check = check_endpoint_info(request.json, ['name'])

    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL patch_menu(?, ?)", [results[0]['id'], request.json.get("name")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify('Client info updated successfully'), 200)
    else: 
       return make_response(jsonify("Sorry, something went wrong"), 500)
    

#Delete menu item

@app.delete('/api/delete_menu')
def delete_menu():
    token = request.headers.get("Authorization")
    print(token)
    results = run_statement("CALL verified_restaurant_token(?)", [token])
    print(results)
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, ['name'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL delete_menu_item(?, ?)", [results[0]['id'], request.json.get("name")])
    print(results)
    if(type(results) == list and len(results) == 0):

        return make_response(jsonify('Delete successful'), 200)
    elif(len(results) > 0):
        return make_response(jsonify("Sorry, password dose not match"), 400)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)

    

#Client order functions

@app.post('/api/client_order')
def post_clientOrder():
    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_token(?)", [token])
    client_id = results[0]['id']
    print(client_id)
   
    if(len(results) == 0):
        return 'token invalid'
    valid_check = check_endpoint_info(request.json, [ 'menu_items', 'restaurant_id'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    menu_items = request.json.get('menu_items')
   
    restaurant_id = request.json.get('restaurant_id')
   
   #Step
    for menu_item in menu_items:
       
        results = run_statement("CALL check_menu_item(?, ?)", [menu_item, restaurant_id])
        print(results)
        if(len(results) ==0):
            return make_response(jsonify('Sorry, something went wrong.'), 400)
    
    #Step2
    results = run_statement("CALL post_order(?, ?)", [client_id, restaurant_id])
    print(results)
    order_id = results[0]['id']
    print(order_id)

    #step3
    for menu_item in menu_items:
      results = run_statement("CALL post_order_menu_item(?, ?)", [order_id, menu_item])
      

    return make_response(jsonify({'order_id':order_id}), 200)




    
@app.get('/api/client_order')
def get_client_order(): 

    token = request.headers.get("Authorization")
    results = run_statement("CALL verified_token(?)", [token])
    print('Check out', results[0]['id'])
    if(len(results) == 0): 
            return 'token invalid'
    
    client_id = results[0]['id']
    print(client_id)
    
    results = run_statement("CALL get_client_order(?)", [client_id])
    if(len(results) == 0): 
            return 'You do not have any orders in the system'
    return make_response(jsonify(results), 200)
    
    
  

    




    


 
app.run(debug=True)