'use strict';

// Declare app level module which depends on views, and components
angular.module('marco', [
  'ngRoute',
  'ngAnimate',
  'marco.index',
  'marco.catalog',
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/'});
}]);

angular.module('marco').controller('CategoryTreeCtrl', function($scope, $http){

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
