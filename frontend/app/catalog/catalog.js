'use strict';

angular.module('marco.catalog', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/catalog', {
    templateUrl: 'catalog/catalog.html',
    controller: 'View2Ctrl'
  });
}])

.controller('View2Ctrl', [function() {

}]);