'use strict';

angular.module('MirrorStore').directive('rsSlider', [function () {
    return {
        'link': function (scope, elem, attrs) {

            if (scope.$last) {
                $(elem.parent()).responsiveSlides({
                    auto: true,
                    pager: true,
                    nav: true,
                    speed: 1000,
                    namespace: "centered-btns"
                });

            }
        }
    };
}]);

angular.module('MirrorStore').directive('scrollOnClick', function () {
    return {
        restrict: 'A',
        link: function (scope, $elm) {
            $elm.on('click', function () {
                $("body").animate({scrollTop: 0}, "slow");
            });
        }
    }
});

angular.module('MirrorStore').directive('marcoPagination', ['$location', '$window', function ($location, $window) {
    return {
        restrict: 'E',
        templateUrl: '/components/templates/pagination.html',
        link: function ($scope, element, attrs) {
            var SHOW_PAGES = 11;

            attrs.$observe('page', function (page) {
                page = eval(page);
                var currPage = page[0];
                var pagesCount = page[1];

                $scope.pages = [];
                if (pagesCount == 1) {
                    return;
                }

                if (pagesCount <= SHOW_PAGES) {
                    for (var i = 1; i <= pagesCount; i++) {
                        $scope.pages.push(i);
                    }
                } else {
                    var leftRange = [1, SHOW_PAGES - 2];
                    var rightRange = [pagesCount - (SHOW_PAGES - 2), pagesCount];

                    if (currPage >= leftRange[0] && currPage < leftRange[1]) {

                        for (var i = leftRange[0]; i <= leftRange[1]; i++) {
                            $scope.pages.push(i)
                        }
                        $scope.pages.push('...');
                        $scope.pages.push(pagesCount);

                    } else if (currPage > rightRange[0] && currPage <= rightRange[1]) {

                        $scope.pages.push(1);
                        $scope.pages.push('...');
                        for (var i = rightRange[0]; i <= rightRange[1]; i++) {
                            $scope.pages.push(i)
                        }

                    } else {
                        $scope.pages.push(1);
                        $scope.pages.push('...');
                        var delta = parseInt((SHOW_PAGES - 4) / 2);
                        var centerRange = [currPage - delta, currPage + delta];

                        for (var i = centerRange[0]; i <= centerRange[1]; i++) {
                            $scope.pages.push(i)
                        }

                        $scope.pages.push('...');
                        $scope.pages.push(pagesCount);
                    }
                }

            });

            $scope.changePage = function (page) {
                $location.search(
                    angular.extend(
                        $location.search(),
                        {page: page}
                    )
                );
            }
        }
    }
}]);

angular.module('MirrorStore').directive('orderingSelector', ['$location', function ($location) {
    return {
        restrict: 'E',
        templateUrl: '/components/templates/ordering.html',
        link: function ($scope, element, attrs) {
            $scope.orderingParams = [
                {'order': '+price', 'title': 'По возрастанию цены'},
                {'order': '-price', 'title': 'По убыванию цены'},
                {'order': '+title', 'title': 'По названию'},
                {'order': '+is_preorder', 'title': 'По наличию'}
            ];

            $scope.defaultOrdering = $scope.orderingParams[3];

            attrs.$observe('ordering', function (ordering) {
                if (ordering) {
                    for (var index in $scope.orderingParams) {
                        if ($scope.orderingParams[index].order === ordering) {
                            break;
                        }
                    }
                    $scope.defaultOrdering = $scope.orderingParams[index];
                }
            });


            $scope.changeOrdering = function () {
                $location.search(
                    angular.extend(
                        $location.search(),
                        {ordering: $scope.defaultOrdering.order}
                    )
                );
            };

        }
    };
}])
;

angular.module('MirrorStore').directive('pageSizeSelector', ['$location', function ($location) {
    return {
        restrict: 'E',
        templateUrl: '/components/templates/page-size.html',
        link: function ($scope, element, attrs) {
            $scope.pageSizes = [12, 24, 36];

            $scope.changePageSize = function () {
                $location.search(
                    angular.extend(
                        $location.search(),
                        {page_size: $scope.pageSize}
                    )
                );
            };
        }
    }
}]);

angular.module('MirrorStore').directive('marcoSidebar', ['Category', function (Category) {
    return {
        restrict: 'E',
        templateUrl: '/components/templates/sidebar.html',
        link: function ($scope, element, attrs) {
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
        }
    }
}]);

angular.module('MirrorStore').directive('marcoImage', [function () {
    return {
        restrict: 'E',
        template: '<img class="{{class}}" src="{{ src }}" alt="{{title}}">',
        link: function ($scope, element, attrs) {
            attrs.$observe('source', function (src) {
                var source = src.split('/');
                source.splice(3,0,attrs.height);
                source.splice(4,0,attrs.width);
                $scope.src = source.join('/');
                $scope.alt = attrs.alt;
                $scope.class = attrs.class;
            });
        }
    }
}]);

angular.module('MirrorStore').directive('marcoAddToCard', function($cookies){
    return {
        restrict: 'E',
        templateUrl: '/components/templates/add-to-card.html',
        link: function($scope, element, attrs){
            $scope.quantity = 1;
            attrs.$observe('id', function(id){
                $scope.addToCard = function(){
                    var card = $cookies.getObject('basket');
                    if(!card){
                        card = {};
                    }

                    if(card[id]){
                        card[id] = card[id] + $scope.quantity;
                    }else {
                        card[id] = $scope.quantity;
                    }

                    $cookies.putObject('basket', card);
                }
            });

        }
    }
});

angular.module('MirrorStore').directive('marcoTopSidebar', function($cookies){
    return {
        restrict: 'E',
        templateUrl: '/components/templates/top-sidebar.html',
        link: function($scope, element, attrs){
            $scope.$watch();
            $scope.basket = 0;

            $scope.$watch(function(){
                var basket = $cookies.getObject('basket');
                var keys = Object.keys(basket);
                var quant = 0;

                for(var key in keys){

                    quant+=basket[keys[key]];
                }

                return quant;
            }, function(v){
                $scope.basket = v;
            });
        }
    }
});


