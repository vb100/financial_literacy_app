import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import FeedScreen from './app/screens/FeedScreen';
import ArticleDetailScreen from './app/screens/ArticleDetailScreen';
import { Article } from './app/types/feed';

export type RootStackParamList = {
  Feed: undefined;
  ArticleDetail: { article: Article };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Feed" component={FeedScreen} options={{ title: 'Career Compass' }} />
        <Stack.Screen name="ArticleDetail" component={ArticleDetailScreen} options={{ title: 'Article' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
