app.controller('ProductsListingController', function($scope, $http){

    $http.get('/api/products/').success(function(data) {
        $scope.products = data.results;

    });
    $scope.abc = '123'

});