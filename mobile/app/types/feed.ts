export interface Article {
  id: number;
  title: string;
  url: string;
  source?: string;
  summary?: string;
  snippet?: string;
  published_at?: string;
  rank: number;
}

export interface FeedResponse {
  feed_date: string;
  articles: Article[];
}
