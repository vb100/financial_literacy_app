import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { RootStackParamList } from '../../App';


type Props = NativeStackScreenProps<RootStackParamList, 'ArticleDetail'>;

export default function ArticleDetailScreen({ route }: Props) {
  const { article } = route.params;
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{article.title}</Text>
      <Text style={styles.source}>{article.source}</Text>
      <Text>{article.summary}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  source: {
    fontSize: 16,
    marginBottom: 12,
  },
});
