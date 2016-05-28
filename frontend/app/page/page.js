angular.module('MirrorStore.page', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/page/:id', {
            templateUrl: 'page/page.html',
            controller: 'pageCtrl'
        });
    }])

    .controller('pageCtrl', function ($rootScope, $routeParams, $scope, Page) {

        Page.get({id: $routeParams.id }, function (page) {
            $rootScope.title =page.title;
            $scope.page = page;
        });

    });