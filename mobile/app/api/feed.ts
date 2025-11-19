import { apiGet } from './client';
import { FeedResponse } from '../types/feed';

export function fetchLatestFeed() {
  return apiGet<FeedResponse>('/feed/latest');
}
