app.controller('ProductsListingController', function($scope, $http){

    $http.get('/api/products/').success(function(data) {
        $scope.products = data;

    });
    

});

app.controller('CatalogController', function($scope, $http, $routeParams){
    var category = $routeParams.category_alias;
    $http.get('/api/products/?category__url=' + category).success(function(data) {
        $scope.products = data;
        console.log(data)
    });


});

app.controller('CategoryTreeController', function($scope, $http){

    $http.get('/api/category/').success(function(data) {
        var sortedCategories = {};
        for(var index in data){
            var parentId = !data[index].parent ? 0 : data[index].parent;
            if(!sortedCategories[parentId]){
                sortedCategories[parentId] = [];
            }
            sortedCategories[parentId].push(data[index]);
        }

        var result = [];
        for (var index in sortedCategories[0]) {
            if (sortedCategories[0][index].id) {
                sortedCategories[0][index].childrens = sortedCategories[sortedCategories[0][index].id]
            }
            result.push(sortedCategories[0][index])
        }

        $scope.categories = result;
    });


});

app.controller('MainSliderController', function ($scope, $http) {

    $scope.result = false;
    $http.get('/api/slider/1').success(function(data) {
        $scope.result = true;
        $scope.images =  data.gallery;
    });


});