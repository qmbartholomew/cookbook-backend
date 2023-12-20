from masonite.routes import Route

ROUTES = [
    Route.group([
        Route.get('/', 'RecipeController@index').name('index'),
        Route.get('/@id', 'RecipeController@show').name('show'),
        Route.post('/', 'RecipeController@create').name('create'),
        Route.put('/@id', 'RecipeController@update').name('update'),
        Route.delete('/@id', 'RecipeController@destroy').name('destroy')
    ], prefix='/recipes', name='recipes')
]
