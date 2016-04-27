'use strict';

// Declare app level module which depends on views, and components
angular.module('marco', [
  'ngRoute',
  'marco.index',
  'marco.catalog',
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/index'});
}]);
