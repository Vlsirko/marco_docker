app.controller('ProductsListingController', function($scope, $http){

    $http.get('/api/products/').success(function(data) {
        $scope.products = data.results;

    });
    

});

app.controller('CategoryTreeController', function($scope, $http){

    $http.get('/api/category/?parent=null').success(function(data) {
        $scope.categories = data;
    });


});

app.controller('MainSliderController', function ($scope, $http) {

    $scope.result = false;
    $http.get('/api/slider/1').success(function(data) {
        $scope.result = true;
        $scope.images =  data.gallery;
    });


});