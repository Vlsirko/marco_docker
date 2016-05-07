'use strict';

// Declare app level module which depends on views, and components
angular.module('MirrorStore', [
  'ngRoute',
  'MirrorStore.index',
  'MirrorStore.catalog',
  'MirrorStore.card',
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/'});
}]);
