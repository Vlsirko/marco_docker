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
  $http.get('/api/products/').success(function(data) {
    $scope.products = data;
  });
  
});