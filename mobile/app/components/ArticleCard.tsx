import React from 'react';
import { Pressable, Text, View, StyleSheet } from 'react-native';
import { Article } from '../types/feed';

interface Props {
  article: Article;
  onPress: () => void;
}

export default function ArticleCard({ article, onPress }: Props) {
  return (
    <Pressable onPress={onPress} style={styles.card}>
      <Text style={styles.title}>{article.title}</Text>
      <Text style={styles.source}>{article.source}</Text>
      <Text style={styles.summary} numberOfLines={2}>
        {article.summary}
      </Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    elevation: 1,
  },
  title: {
    fontWeight: '600',
    marginBottom: 4,
  },
  source: {
    fontSize: 12,
    color: '#666',
    marginBottom: 6,
  },
  summary: {
    fontSize: 14,
  },
});
