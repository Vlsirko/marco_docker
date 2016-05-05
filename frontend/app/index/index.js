'use strict';

angular.module('marco.index', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'index/index.html',
    controller: 'IndexCtrl'
  });
}])

.controller('IndexCtrl', function($scope, $http) {

  $scope.result = false;
  $http.get('/api/slider/1').success(function(data) {
    $scope.result = true;
    $scope.images =  data.gallery;
  });

}).controller('NewProductsCtrl', function($scope, $http){
  $scope.products = false;
  $http.get('/api/products/?page_size=6&is_new=True&ordering=-time_add').success(function(data) {
    $scope.products = data.results;

  });
  
}).controller('SaleProductsCtrl', function($scope, $http){
  $scope.products = false;
  $http.get('/api/products/?page_size=6&is_sale=True&ordering=-time_add').success(function(data) {
    $scope.products = data.results;
  });

});