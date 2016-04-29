'use strict';

angular.module('marco.catalog', ['ngRoute', 'ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/catalog/:category_alias', {
    templateUrl: 'catalog/catalog.html',
    controller: 'catalogCtrl'
  });
}])

.controller('catalogCtrl', function($scope, $http, $routeParams) {
  var category = $routeParams.category_alias;
  $http.get('/api/products/?category__url=' + category).success(function(data) {
    $scope.products = data;
    console.log(data)
  });
});