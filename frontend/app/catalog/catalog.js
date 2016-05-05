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
  var page = $routeParams.page;
  var pageString = page ? '&page=' . page : '';
  $http.get('/api/products/?category__url=' + category + pageString).success(function(data) {
    $scope.products = data.results;
  });
});