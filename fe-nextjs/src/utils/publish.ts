export const checkPublished = async (): Promise<boolean> => {
  return (window.location.href).includes('http')
}