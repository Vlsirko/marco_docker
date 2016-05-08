'use strict';

// Declare app level module which depends on views, and components
angular.module('MirrorStore', [
    'ngRoute',
    'ngResource',
    'ngAnimate',
    'ngSanitize',
    'services',
    'MirrorStore.index',
    'MirrorStore.catalog',
    'MirrorStore.card'
]).config(['$routeProvider', function ($routeProvider) {
    $routeProvider.otherwise({redirectTo: '/'});
}]).config(function($httpProvider) {
    $httpProvider.interceptors.push(function($q) {
        var realEncodeURIComponent = window.encodeURIComponent;
        return {
            'request': function(config) {
                window.encodeURIComponent = function(input) {
                    return realEncodeURIComponent(input).split("%2B").join("+");
                };
                return config || $q.when(config);
            },
            'response': function(config) {
                window.encodeURIComponent = realEncodeURIComponent;
                return config || $q.when(config);
            }
        };
    });
});

angular.module('MirrorStore').controller('MainCtrl', function ($scope, Category) {

    Category.query().$promise.then(function (data) {
        data = JSON.parse(JSON.stringify(data));
        var sortedCategories = {};
        for (var index in data) {
            var parentId = !data[index].parent ? 0 : data[index].parent;
            if (!sortedCategories[parentId]) {
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
